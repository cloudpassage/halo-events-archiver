# CloudPassage Halo Events Archiver


[![Test Coverage](https://codeclimate.com/github/cloudpassage/halo-events-archiver/badges/coverage.svg)](https://codeclimate.com/github/cloudpassage/halo-events-archiver/coverage)

[![Code Climate](https://codeclimate.com/github/cloudpassage/halo-events-archiver/badges/gpa.svg)](https://codeclimate.com/github/cloudpassage/halo-events-archiver)

[![Issue Count](https://codeclimate.com/github/cloudpassage/halo-events-archiver/badges/issue_count.svg)](https://codeclimate.com/github/cloudpassage/halo-events-archiver)

## What it does


Downloads one day's events from the Halo API.  10,000 events per file, gzipped.

## When would you use this sort of thing?


If your compliance requirements bind you to a longer retention period than your
Halo account provides, and you need to get your events into cold storage.

## How do use it

It's all bundled in a Docker container, so you just need to run it with the
proper arguments.  Specifically, you'll need to pass in the API authentication
key and secret as well as the date to retrieve events for, as environment
variables.

You'll also need to mount a directory from the base OS into the
container so that your results won't be bound up inside the container when it
stops, assuming that you want the events archived locally.  If you want your
events stored in S3, define the AWS-oriented environment variables
(AWS_S3_BUCKET, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY) and don't worry about
mounting in a directory for the retrieved events.  The S3 bucket must exist
before running this tool.  It doesn't attempt to create one for you.  Follow the
principle of least privilege: Only use an API key for AWS that has access to the
S3 bucket you need to drop the events into.

### Define the following environment variables:

* HALO_API_KEY: sometimes referred to as Key ID
* HALO_API_SECRET_KEY
* HALO_API_HOSTNAME (optional, defaults to `api.cloudpassage.com`)
* TARGET_DATE: Date to export events for, in ISO 8601 format, like this:
"2016-12-01" (optional, defaults to yesterday)
* LOCAL_OUTPUT_DIR: absolute path to the directory you want your events to land
in
* AWS_S3_BUCKET: If this is defined, the tool will attempt to upload the
gzipped files to S3.  If this is set and you don't pass in AWS API credentials,
it will fail.
* AWS_ACCESS_KEY_ID
* AWS_SECRET_ACCESS_KEY

### Run it like this for local storage:


        docker run -it --rm \
            -e HALO_API_KEY=$HALO_API_KEY \
            -e HALO_API_SECRET_KEY=$HALO_API_SECRET_KEY \
            -e TARGET_DATE=$TARGET_DATE \
            -v $LOCAL_OUTPUT_DIR:/var/events \
            docker.io/halotools/halo-events-archiver


### And like this for S3 storage:



        docker run -it --rm \
            -e HALO_API_KEY=$HALO_API_KEY \
            -e HALO_API_SECRET_KEY=$HALO_API_SECRET_KEY \
            -e TARGET_DATE=$TARGET_DATE \
            -e AWS_S3_BUCKET=$AWS_S3_BUCKET \
            -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
            -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
            docker.io/halotools/halo-events-archiver


<!---
#CPTAGS:community-supported automation archive
#TBICON:images/python_icon.png
-->
