deployed = {"ec2", "rds", "s3"}
expected = {"ec2", "s3", "lambda"}
missing  = expected - deployed    # in expected but not deployed → {"lambda"}
extra    = deployed - expected 

print(missing)
print(extra)