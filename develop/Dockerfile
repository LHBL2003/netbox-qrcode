ARG python_ver=3.12
FROM python:${python_ver}

ARG netbox_ver=main
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /opt

RUN cat /etc/os-release

# For Data Matrix
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libdmtx-dev \
        $(apt-cache show libdmtx0b >/dev/null 2>&1 && echo libdmtx0b || echo libdmtx0a) \
        git \
        gcc \
        libc-dev \
        build-essential && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install setuptools

# -------------------------------------------------------------------------------------
# Install NetBox
# -------------------------------------------------------------------------------------
RUN git clone --single-branch --branch ${netbox_ver} https://github.com/netbox-community/netbox.git /opt/netbox/ && \
    cd /opt/netbox/ && \
    pip install -r /opt/netbox/requirements.txt

# -------------------------------------------------------------------------------------
# Install Netbox Plugin
# -------------------------------------------------------------------------------------
RUN mkdir -p /source
WORKDIR /source
COPY . /source

#RUN pip install -r requirements.txt
RUN python -m pip install -e .

WORKDIR /opt/netbox/netbox/
