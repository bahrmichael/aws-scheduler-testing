# aws-scheduler-testing

This is a project to help with testing and performance measurements of the [aws-scheduler](https://github.com/bahrmichael/aws-scheduler).

## Setup

### Prerequisites
You must have the following tools installed:
- serverless framework 1.48.3 or later
- node
- npm
- python3
- pip

Run `setup/init_table.py <stage>` to setup the database. Replace `<stage>` with the stage of your application (e.g. `dev`).

Run `setup/init_output_topic.py <stage>`. Replace `<stage>` with the stage of your application (e.g. `dev`).

### Deploy
1. Navigate into the project folder
2. With a tooling of your choice create and activate a venv
3. `pip install -r requirements.txt`
4. `npm i serverless-python-requirements`
5. `sls deploy`
6. Optional: `pip install matplotlib` if you want to plot the delays later 

Wait for the deployment to finish. Test the service by first attaching a function to the output topic and then send a few events to the input topic.

## Run it

Once you created the database and topic and deployed the stack, run the producer with `python producer.py <your-output-topic> [amount] [input-topic]`. Replace `<your-output-topic>` with the arn of the topic you created during the setup. You may specify a second argument to set the number of events, the default is 100. You may specify a third argument to use a different input topic. You may also trigger the function from the aws lambda console.

Run `sls logs -f consumer -t` to tail the logs. You may receive an error that the log stream does not exist until the first event has arrived.

After 5 minutes all events should have arrived at the output topic and the measured delays are stored in the database. You can now run `python evaluate_measurement.py` to plot the delays.
