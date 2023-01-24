# python3.8 lambda base image
FROM public.ecr.aws/lambda/python:3.9-x86_64

RUN  \
    yum -y update && \
    yum install -y \
    libXext \
    libSM \
    libXrender \
    libgomp1 \
    yum clean all && rm -rf /var/cache/yum/*
    
# copy requirements.txt to container
COPY requirements.txt ./

# installing dependencies
RUN pip3 install -r requirements.txt

# Copy function code to container
COPY app.py ./

# setting the CMD to your handler file_name.function_name
CMD [ "app.handler" ]