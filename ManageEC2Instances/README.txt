This will set the expire-on tag for instances that match the filter criteria.
The filter criteria is purposely hard corded for now. You can simply go in and edit the pattern variable.
I might make it a parameter later.

The only option to this script is the -d option which takes a integer that represents how many days into the future to set the expiration date to.

If you don't touch it, the default is 30...

Also, before you can use the script you have to have your .aws/credentials and .aws/config files configured.
See the following link for details.
http://boto3.readthedocs.io/en/latest/guide/quickstart.html

The whole thing is a package... I'll admit there is little need for a package given only one module is available but it might grow in the future.


