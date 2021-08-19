import itertools

import clearml
import plotly.figure_factory as ff


def plot(tasks):
    df = [dict(Task=task.name, Start=task.data.started, Finish=task.data.completed, Resource=task.status)
          for task in tasks]

    fig = ff.create_gantt(df,index_col='Resource', show_colorbar=True,
                          group_tasks=True)
    fig.show()


task = clearml.Task.init(project_name='grachev', task_name='Simple clearml task')
if clearml.config.running_remotely():
    print('waiting')
    import time
    time.sleep(30)
    exit(0)
else:
    print('Adding tasks')
    task._wait_for_repo_detection(timeout=300.)
    task1 = clearml.Task.clone(task)
    task1.name = '_2gpu'
    clearml.Task.enqueue(task=task1, queue_name='_2gpu')

    task2 = clearml.Task.clone(task)
    task2.name = '_1gpu gpus=0'
    task2.set_user_properties(gpus=0)
    clearml.Task.enqueue(task=task2, queue_name='_1gpu')

    task3 = clearml.Task.clone(task)
    task3.name = '_2gpu gpus=0'
    task3.set_user_properties(gpus=0)
    clearml.Task.enqueue(task=task3, queue_name='_2gpu')

    task4 = clearml.Task.clone(task)
    task4.name = '_2gpu gpus=1'
    task4.set_user_properties(gpus=1)
    clearml.Task.enqueue(task=task4, queue_name='_2gpu')

    task5 = clearml.Task.clone(task)
    task5.name = '_1gpu'
    clearml.Task.enqueue(task=task5, queue_name='_1gpu')

    tasks = [task1, task2, task3, task4, task5]
    for task in tasks:
        Status = clearml.Task.TaskStatusEnum
        task.wait_for_status(status=(Status.completed,),
                             raise_on_status=(Status.stopped, Status.closed, Status.failed), check_interval_sec=5)
        data = task.data
        print(task.name, data.started, data.completed)
        task.reload()

    plot(tasks)

    sorted_times = [task1.data.started,
                   task2.data.started, task1.data.completed,
                   task3.data.started, task2.data.completed,
                   task4.data.started, task3.data.completed,
                   task4.data.completed]

    if sorted(sorted_times) != sorted_times:
        print(f'Times should be in incremetned order:\n{sorted_times}')

