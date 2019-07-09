'''
This script is intended to facilitate providing feedback to students using GitHub pull
	requests. This script should be run before starting editing code. Its counterpart,
	gitHubFeedbackFinish.py should be run when done and before creating the pull request.
	
This script takes a single argument which is the URL of the student repository. It is
	most easily copied from SpeedGrader in Canvas.
	
The following commands are run:
	git branch feedback
	git checkout feedback
	git remote set-url origin <specified URL>
'''

import sys
import subprocess

if len(sys.argv) < 2:
	print("specify the URL for the remote origin of the student repository as an argument to the script")
	sys.exit()

result = subprocess.run(['git', 'branch', 'feedback'],  stdout=subprocess.PIPE)
print(result.stdout.decode('utf-8'))
result = subprocess.run(['git', 'checkout', 'feedback'],  stdout=subprocess.PIPE)
print(result.stdout.decode('utf-8'))
result = subprocess.run(['git', 'remote', 'set-url', 'origin', sys.argv[1]],  stdout=subprocess.PIPE)
print(result.stdout.decode('utf-8'))
