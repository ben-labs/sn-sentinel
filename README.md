[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)



# sn-sentinel
Monitoring and Alert for ServiceNow On-Premise Patches

## Description
On-Premise implementations of ServiceNow will require patching / upgrades during the course of
deployment. Admins need to rely on ServiceNow annoucements / email alerts for new patches released.
It is sometimes critical for patches to be deployed in a timely manner (ie: governance). SN-Sentinel was
created to help monitor ServiceNow's FTP site and alert admin teams via telegram of availability.

This set of code mainly consists of 2 classes that help to acheive this.
- blab.sentinel.Ftp
- blab.sentinel.Telegram

There also exists an example folder showing how you can use the classes.

## Setting up dev (You will need this)
Set pythonpath using the following
`export PYTHONPATH=$(pwd)/src:$PYTHONPATH`

## Note
- These modules are currently still in beta

## Release History
version 0.1.0:
- Initial working copy with Ftp module

version 0.1.1:
- added in Telegram class
- added in examples
- switched to properties