# AWS Fargate Python Flask App

A reference project to deploy a Python Flask app onto Amazon ECS on AWS Fargate with Terraform. Inspired by [this](https://aws.amazon.com/blogs/opensource/deploying-python-flask-microservices-to-aws-using-open-source-tools/) AWS tutorial

A todo app creating, and retrieving data from Amazon RDS

![AWS Architecture](img/aws-flask-rds.JPG)

## Pre-requisite

- Make sure you have installed Python 3, [pip](https://pip.pypa.io/en/stable/installing/), [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli), [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-mac.html#cliv2-mac-prereq), and configured a `default` AWS CLI profile (see doc [here](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-profiles))

```bash
terraform -help # prints Terraform options
which aws # prints /usr/local/bin/aws
aws --version # prints aws-cli/2.0.36 Python/3.7.4 Darwin/18.7.0 botocore/2.0.0
aws configure # configure your AWS CLI profile
python3 --version # prints Python 3 version
pip3 --version # prints pip version
```

## Run/Build app locally

- In a seperate terminal window, run `docker-compose -f docker-compose.dev.yml up` to run PostgreSQL database inside a container. Then, return to the original terminal window and run the following commands:

```bash
virtualenv -p /usr/bin/python3 venv # create new virtual environment venv
source venv/bin/activate # activate venv
pip3 install -r requirements.txt # installs python packages
python3 manage.py # visit app at http://localhost:5000/ping
deactivate # deactivates venv
```

### Install new packages

```bash
pip3 install boto # installs new Python package
pip3 freeze > requirements.txt # updates requirements.txt
```

### Run app in container

- Run `docker-compose up` to start app in container. Alternatively, you may choose to build, and run the `api` app image:

```bash
docker build -t matlau/python-flask-aws:latest . # build Docker image
docker run -p 5000:5000 matlau/python-flask-aws # visit app at http://localhost:5000/ping
```

## Configuration

- Create an [S3 bucket](https://www.terraform.io/docs/language/settings/backends/s3.html) to store Terraform state. Populate bucket name in `01-main.tf`

- Create a secret on [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) named `RDSPostgresPassword` with key `POSTGRES_PASSWORD`, and your database password as value

- Populate `terraform.tfvars`:

```bash
default_region      = "<YOUR_AWS_DEFAULT_REGION>"
app_name            = "<GIVE_YOUR_APP_A_NAME!>"
environment         = "<ENVIRONMENT_NAME>"
```

## Deploy AWS stack

```bash
cd deploy # change to deploy directory
terraform init # initialises Terraform
terraform apply # deploys AWS stack. See output for API url
terraform destroy # destroys AWS stack
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

If you find this project helpful, please give a :star: or even better buy me a coffee :coffee: :point_down: because I'm a caffeine addict :sweat_smile:

<a href="https://www.buymeacoffee.com/matlau" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

## License

[MIT](https://choosealicense.com/licenses/mit/)
