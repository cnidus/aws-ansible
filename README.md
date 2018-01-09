
-- Links and sources:
  https://aws.amazon.com/blogs/mt/running-ansible-playbooks-using-ec2-systems-manager-run-command-and-state-manager/

  https://medium.com/@jacoelho/ansible-in-aws-lambda-980bb8b5791b

  http://docs.aws.amazon.com/systems-manager/latest/userguide/rc-sns-notifications.html

  https://viewsby.wordpress.com/2014/11/25/ansible-disable-gather-facts/

-- Local ansible execution
    ansible-playbook -i "localhost," -c local get_yumlist.yml

-- Playbook execution via SSM connection plugin
    cd ssm_plugin
    ansible-playbook -i hosts get_yumlist_sml.yml

-- Run Cmd
    aws ssm send-command --instance-ids "i-03a9ff4db1e58da23" --document-name "AWS-RunShellScript" --comment "IP config" --parameters "commands=ifconfig" --output text


    aws ssm send-command --document-name "AWS-RunAnsiblePlaybook" --instance-ids "i-03a9ff4db1e58da23" "i-080feed63350968ce" "i-081c9adff8f0cde0d" --max-concurrency "3" --max-errors "1" --parameters '{"extravars":["SSM=True"],"check":["False"],"playbookurl":["s3://snap-ansible-testing/get_yumlist.yml"]}' --timeout-seconds 600 --region us-east-1 --output-s3-bucket-name "snap-ansible-testing"


-- Requirements
Base should have ansible, ssm agent and boto3 installed
    sudo pip install ansible
    sudo pip install boto3
