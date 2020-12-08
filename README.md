<!-- for install pakage :- python3.6 -m pip install --system --target ./ requests -->
<!-- python3.6 -m pip install --system --target /home/abdul/Ansible/test/Lib/ -r requirements.txt -->

<!-- Note:- if we get an error then make sure in our /home/user/.ansible/tmp directory should be empty -->

<!-- Steps:- 
1.  prerequisite:- 
    Python Version :- Python 3.6.9
    botocore Version :- botocore 1.19.30 
    boto3 :- boto3 1.16.30
    ansible :- ansible 2.10.3
    aws cli :- 1 or 2 which you want
    ansible-galaxy collection install community.general
    ansible-galaxy collection install amazon.aws

2.  In the build directory our zip will be create hear.
3.  In the include directory we put two file on is copy_to_s3 which make zip and push it to s3 bucket,  second is init_workspace which crate on directory and copy all files into it directory.
4.  Lib directory hear we have our requirements.txt or pythone files.
5.  pakage in this directory our all file and pakage will be store.
6.  Then last we have to run ansible-playbook "yml file name" 

    




    pip install botocore
    pip install boto3
    sudo apt install python3.8
    sudo apt-get -y install python3-pip -->