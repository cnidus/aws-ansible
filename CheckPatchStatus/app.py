from chalice import Chalice
import urllib2
import json
import boto3

s3 = boto3.client('s3', region_name='us-east-1')

ConvertURL = "https://api.rss2json.com/v1/api.json?rss_url="
RSSFeed = "https://alas.aws.amazon.com/alas.rss"
URL = ConvertURL + RSSFeed
BUCKET_NAME = "snap-ansible-testing"

app = Chalice(app_name='CheckPatchStatus')


@app.route('/GetRSSSecurityBulletins')
def GetRSSSecurityBulletins():
    response = urllib2.urlopen(URL)
    data = json.loads(response.read())

    print data

    return data['items']

@app.route('/GetXMLSecurityBulletins')
def GetXMLSecurityBulletins():


    return


@app.route('/GetInstancePatches/{InstanceID}', methods=['GET'])
def GetInstancePatches(InstanceID):

    FileName = "eb88201f-1f36-4150-bfac-46f02ab1d171/i-003db512f0a358e1d/awsrunShellScript/runShellScript/stdout"

    #Read Ansible results from S3
    try:
        S3Object = s3.get_object(Bucket=BUCKET_NAME, Key=FileName)
        # CachedTotals = json.loads(S3Object['Body'].read().decode('utf-8'))
        print "Ansible output found on s3"
        S3Body = S3Object['Body'].read().decode('utf-8')
        print S3Body
        YUMPkgs = str(str(S3Body).split('"results": ',)[1]).split('}}PLAY RECAP *',)[0]
        print YUMPkgs
        pass
    except Exception as e:
        print "No Ansible output found on s3: " + str(e)
        S3Body = "Error loading S3 ansible output"

    return YUMPkgs
