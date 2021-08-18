import clearml
task = clearml.Task.init(project_name='grachev', task_name='Simple clearml task')
if clearml.config.running_remotely():
    print('waiting')
    import time
    time.sleep(60)
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

    print(task1.started, task2.started, task3.started, task4.started, task5.started)
    print(task1.completed, task2.completed, task3.completed, task4.completed, task5.completed)