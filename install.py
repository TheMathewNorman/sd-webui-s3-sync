import launch

if not launch.is_installed("awscli"):
    launch.run_pip("install awscli", "requirements for S3 Sync")
