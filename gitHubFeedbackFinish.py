'''
This script is intended to facilitate providing feedback to students using GitHub pull
	requests. This script should be run when done editing code. Its counterpart,
	gitHubFeedbackStart.py should be run before starting to edit code.
	
The following commands are run:
	git add -A
	git commit -m "feedback"
	git push --set-upstream origin feedback
'''

import sys
import subprocess

result = subprocess.run(['git', 'add', '-A'],  stdout=subprocess.PIPE)
print(result.stdout.decode('utf-8'))
result = subprocess.run(['git', 'commit', '-m', 'feedback'],  stdout=subprocess.PIPE)
print(result.stdout.decode('utf-8'))
result = subprocess.run(['git', 'push', '--set-upstream', 'origin', 'feedback'],  stdout=subprocess.PIPE)
print(result.stdout.decode('utf-8'))
