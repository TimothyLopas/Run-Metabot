from robocorp.tasks import task
import subprocess
import os

@task
def minimal_task():

    # # Option 1 using the os.system commands
    # # While this is the simplest this also provides the least options
    # folder = os.chdir("/Users/tim/Documents/Robot Tests/No Data Leaving Prem Bot Run/metarobot")
    # print(f"Folder navigation code: {folder}")
    # metabot_run = os.system("rcc run --space metarobot --task metarobot")
    # print(f"Metarobot run code: {metabot_run}")

    
    # # Option 2 using subprocess.run
    # # A highly flexible option that provides the developer many choices
    # command = ["rcc", "run", "--space", "metarobot", "--task", "metarobot"]
    # result = subprocess.run(command, capture_output=True, text=True, cwd=r'/Users/tim/Documents/Robot Tests/No Data Leaving Prem Bot Run/metarobot')
    # print("Output:", result.stdout)
    # print("Errors:", result.stderr)


    # Option 3 using subprocess.Popen
    # This is the most complex option but provides the developer the most flexibility
    metbot_run = subprocess.Popen(["rcc run --space metarobot --task metarobot"], shell=True, cwd=r"/Users/tim/Documents/Robot Tests/No Data Leaving Prem Bot Run/metarobot")
    output, errors = metbot_run.communicate()
    metbot_run.wait()
    print(output)
    print(errors)

