from datetime import datetime
from typing import Callable, IO, List, Dict, Union, Any

from boto3.resources.collection import ResourceCollection
from boto3.s3.transfer import TransferConfig
from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter

from mypy_boto3_builder.structures import (
    TypeAnnotation,
    InternalImport,
    AnnotationWrapper,
)

TYPE_MAP: Dict[str, TypeAnnotation] = {
    "bytes": bytes,
    "blob": bytes,
    "boolean": bool,
    "function": Callable[..., Any],
    "botocore or boto3 Client": BaseClient,
    "datetime": datetime,
    "timestamp": datetime,
    "dict": Dict[str, Any],
    "structure": Dict[str, Any],
    "map": Dict[str, Any],
    "float": float,
    "double": float,
    "int": int,
    "integer": int,
    "long": int,
    "a file-like object": IO[Any],
    "seekable file-like object": IO[Any],
    "list": List[Any],
    "L{botocore.paginate.Paginator}": Paginator,
    ":py:class:`ResourceCollection`": ResourceCollection,
    "JSON serializable": str,
    "string": str,
    "str": str,
    "boto3.s3.transfer.TransferConfig": TransferConfig,
    "botocore.waiter.Waiter": Waiter,
    "bytes or seekable file-like object": Union[bytes, IO],
    "str or dict": Union[str, Dict],
    "list(string)": List[str],
    "list of str": List[str],
    "None": "None",
    ":py:class:`ec2.NetworkAcl`": "'NetworkAcl'",
    ":py:class:`EC2.NetworkAcl`": "'NetworkAcl'",
    "list(:py:class:`ec2.InternetGateway`)": "List['InternetGateway']",
    ":py:class:`iam.UserPolicy`": "'UserPolicy'",
    ":py:class:`IAM.UserPolicy`": "'UserPolicy'",
    "list(:py:class:`iam.VirtualMfaDevice`)": "List['VirtualMfaDevice']",
    "list(:py:class:`ec2.Image`)": "List['Image']",
    "list(:py:class:`cloudwatch.Alarm`)": "List['Alarm']",
    "list(:py:class:`opsworks.Layer`)": "List['Layer']",
    ":py:class:`iam.GroupPolicy`": "'GroupPolicy'",
    ":py:class:`IAM.GroupPolicy`": "'GroupPolicy'",
    "list(:py:class:`iam.SigningCertificate`)": "List['SigningCertificate']",
    "list(:py:class:`ec2.Volume`)": "List['Volume']",
    "list(:py:class:`ec2.VpcPeeringConnection`)": "List['VpcPeeringConnection']",
    ":py:class:`ec2.Subnet`": "'Subnet'",
    ":py:class:`EC2.Subnet`": "'Subnet'",
    "list(:py:class:`iam.ServerCertificate`)": "List['ServerCertificate']",
    "list(:py:class:`ec2.VpcAddress`)": "List['VpcAddress']",
    ":py:class:`sns.PlatformEndpoint`": "'PlatformEndpoint'",
    ":py:class:`SNS.PlatformEndpoint`": "'PlatformEndpoint'",
    ":py:class:`s3.MultipartUpload`": InternalImport("MultipartUpload", "s3"),
    ":py:class:`glacier.MultipartUpload`": "'MultipartUpload'",
    ":py:class:`Glacier.MultipartUpload`": "'MultipartUpload'",
    ":py:class:`S3.MultipartUpload`": InternalImport("MultipartUpload", "s3"),
    "list(:py:class:`ec2.Subnet`)": "List['Subnet']",
    ":py:class:`opsworks.Layer`": "'Layer'",
    ":py:class:`OpsWorks.Layer`": "'Layer'",
    "list(:py:class:`iam.MfaDevice`)": "List['MfaDevice']",
    "list(:py:class:`glacier.Job`)": "List['Job']",
    "list(:py:class:`iam.RolePolicy`)": "List['RolePolicy']",
    "list(:py:class:`iam.InstanceProfile`)": "List['InstanceProfile']",
    "list(:py:class:`ec2.Instance`)": "List['Instance']",
    ":py:class:`glacier.Vault`": "'Vault'",
    ":py:class:`Glacier.Vault`": "'Vault'",
    ":py:class:`ec2.SecurityGroup`": "'SecurityGroup'",
    ":py:class:`EC2.SecurityGroup`": "'SecurityGroup'",
    ":py:class:`ec2.RouteTable`": "'RouteTable'",
    ":py:class:`EC2.RouteTable`": "'RouteTable'",
    "list(:py:class:`dynamodb.Table`)": "List['Table']",
    "list(:py:class:`ec2.Snapshot`)": "List['Snapshot']",
    "list(:py:class:`sqs.Message`)": "List['Message']",
    "list(:py:class:`iam.Role`)": "List['Role']",
    ":py:class:`glacier.Job`": "'Job'",
    ":py:class:`Glacier.Job`": "'Job'",
    "list(:py:class:`cloudwatch.Metric`)": "List['Metric']",
    "list(:py:class:`iam.Policy`)": "List['Policy']",
    "list(:py:class:`ec2.ClassicAddress`)": "List['ClassicAddress']",
    "list(:py:class:`iam.User`)": "List['User']",
    "list(:py:class:`iam.GroupPolicy`)": "List['GroupPolicy']",
    "list(:py:class:`iam.PolicyVersion`)": "List['PolicyVersion']",
    "list(:py:class:`sns.Topic`)": "List['Topic']",
    ":py:class:`iam.LoginProfile`": "'LoginProfile'",
    ":py:class:`IAM.LoginProfile`": "'LoginProfile'",
    "list(:py:class:`iam.UserPolicy`)": "List['UserPolicy']",
    "list(:py:class:`cloudformation.Event`)": "List['Event']",
    ":py:class:`cloudformation.Event`": "'Event'",
    ":py:class:`CloudFormation.Event`": "'Event'",
    "list(:py:class:`s3.MultipartUpload`)": AnnotationWrapper(
        parent=List, children=(InternalImport("MultipartUpload", "s3"),),
    ),
    "list(:py:class:`glacier.MultipartUpload`)": "List['MultipartUpload']",
    "list(:py:class:`sns.Subscription`)": "List['Subscription']",
    ":py:class:`iam.PolicyVersion`": "'PolicyVersion'",
    ":py:class:`IAM.PolicyVersion`": "'PolicyVersion'",
    "list(:py:class:`~boto3.resources.base.ServiceResource`)": "List[Boto3ServiceResource]",
    "list(:py:class:`ec2.NetworkInterface`)": "List['NetworkInterface']",
    "list(:py:class:`s3.ObjectVersion`)": AnnotationWrapper(
        parent=List, children=(InternalImport("ObjectVersion", "s3"),),
    ),
    "list(:py:class:`ec2.SecurityGroup`)": "List['SecurityGroup']",
    "list(:py:class:`sqs.Queue`)": "List['Queue']",
    "list(:py:class:`ec2.PlacementGroup`)": "List['PlacementGroup']",
    "list(:py:class:`ec2.Vpc`)": "List['Vpc']",
    "list(:py:class:`ec2.RouteTable`)": "List['RouteTable']",
    "list(:py:class:`glacier.Vault`)": "List['Vault']",
    "list(:py:class:`iam.Group`)": "List['Group']",
    ":py:class:`iam.Group`": "List['Group']",
    ":py:class:`ec2.Image`": "'Image'",
    ":py:class:`EC2.Image`": "'Image'",
    ":py:class:`ec2.Route`": "'Route'",
    ":py:class:`EC2.Route`": "'Route'",
    ":py:class:`ec2.VpcPeeringConnection`": "'VpcPeeringConnection'",
    ":py:class:`EC2.VpcPeeringConnection`": "'VpcPeeringConnection'",
    "list(:py:class:`cloudformation.Stack`)": "List['Stack']",
    "list(:py:class:`opsworks.Stack`)": "List['Stack']",
    ":py:class:`iam.MfaDevice`": "'MfaDevice'",
    ":py:class:`IAM.MfaDevice`": "'MfaDevice'",
    "list(:py:class:`s3.Bucket`)": AnnotationWrapper(
        parent=List, children=(InternalImport("Bucket", "s3"),),
    ),
    "list(:py:class:`sns.PlatformEndpoint`)": "List['PlatformEndpoint']",
    ":py:class:`ec2.Snapshot`": "'Snapshot'",
    ":py:class:`EC2.Snapshot`": "'Snapshot'",
    "list(:py:class:`ec2.DhcpOptions`)": "List['DhcpOptions']",
    "list(:py:class:`ec2.NetworkAcl`)": "List['NetworkAcl']",
    "list(:py:class:`ec2.KeyPairInfo`)": "List['KeyPairInfo']",
    "list(:py:class:`cloudformation.StackResourceSummary`)": "List['StackResourceSummary']",
    ":py:class:`dynamodb.Table`": "'Table'",
    ":py:class:`DynamoDB.Table`": "'Table'",
    ":py:class:`iam.AccessKeyPair`": "'AccessKeyPair'",
    ":py:class:`IAM.AccessKeyPair`": "'AccessKeyPair'",
    "list(:py:class:`iam.SamlProvider`)": "List['SamlProvider']",
    ":py:class:`glacier.Archive`": "'Archive'",
    ":py:class:`Glacier.Archive`": "'Archive'",
    ":py:class:`ec2.NetworkInterface`": "'NetworkInterface'",
    ":py:class:`EC2.NetworkInterface`": "'NetworkInterface'",
    "list(:py:class:`iam.AccessKey`)": "List['AccessKey']",
    ":py:class:`sns.Subscription`": "'Subscription'",
    ":py:class:`SNS.Subscription`": "'Subscription'",
    "list(:py:class:`s3.MultipartUploadPart`)": "List['MultipartUploadPart']",
    ":py:class:`iam.ServerCertificate`": "'ServerCertificate'",
    ":py:class:`IAM.ServerCertificate`": "'ServerCertificate'",
    "list(:py:class:`ec2.Tag`)": "List['Tag']",
    ":py:class:`cloudwatch.Alarm`": "'Alarm'",
    ":py:class:`CloudWatch.Alarm`": "'Alarm'",
    ":py:class:`EC2.PlacementGroup`": "'PlacementGroup'",
    ":py:class:`ec2.PlacementGroup`": "'PlacementGroup'",
    ":py:class:`EC2.Vpc`": "'Vpc'",
    ":py:class:`ec2.Vpc`": "'Vpc'",
    ":py:class:`S3.BucketVersioning`": "'BucketVersioning'",
    ":py:class:`IAM.User`": "'User'",
    ":py:class:`iam.User`": "'User'",
    ":py:class:`sns.Topic`": "'Topic'",
    ":py:class:`SNS.Topic`": "'Topic'",
    ":py:class:`iam.Policy`": "'Policy'",
    ":py:class:`IAM.Policy`": "'Policy'",
    ":py:class:`S3.BucketCors`": "'BucketCors'",
    ":py:class:`OpsWorks.Stack`": "'Stack'",
    ":py:class:`CloudFormation.Stack`": "'Stack'",
    ":py:class:`opsworks.Stack`": "'Stack'",
    ":py:class:`cloudformation.Stack`": "'Stack'",
    ":py:class:`IAM.SigningCertificate`": "'SigningCertificate'",
    ":py:class:`iam.SigningCertificate`": "'SigningCertificate'",
    ":py:class:`S3.ObjectVersion`": InternalImport("ObjectVersion", "s3"),
    ":py:class:`S3.BucketPolicy`": InternalImport("BucketPolicy", "s3"),
    ":py:class:`EC2.RouteTableAssociation`": "'RouteTableAssociation'",
    ":py:class:`ec2.RouteTableAssociation`": "'RouteTableAssociation'",
    ":py:class:`IAM.RolePolicy`": "'RolePolicy'",
    ":py:class:`IAM.CurrentUser`": "'CurrentUser'",
    ":py:class:`EC2.InternetGateway`": "'InternetGateway'",
    ":py:class:`ec2.InternetGateway`": "'InternetGateway'",
    ":py:class:`sns.PlatformApplication`": "'PlatformApplication'",
    ":py:class:`SNS.PlatformApplication`": "'PlatformApplication'",
    ":py:class:`CloudWatch.Metric`": "'Metric'",
    ":py:class:`IAM.Group`": "'Group'",
    ":py:class:`OpsWorks.StackSummary`": "'StackSummary'",
    ":py:class:`IAM.AssumeRolePolicy`": "'AssumeRolePolicy'",
    ":py:class:`S3.Object`": InternalImport("Object", "s3"),
    ":py:class:`s3.Object`": InternalImport("Object", "s3"),
    ":py:class:`CloudFormation.StackResourceSummary`": "'StackResourceSummary'",
    ":py:class:`S3.BucketWebsite`": InternalImport("BucketWebsite", "s3"),
    ":py:class:`SQS.Queue`": "'Queue'",
    ":py:class:`sqs.Queue`": "'Queue'",
    ":py:class:`S3.MultipartUploadPart`": InternalImport("MultipartUploadPart", "s3"),
    ":py:class:`ec2.KeyPairInfo`": "'KeyPairInfo'",
    ":py:class:`EC2.KeyPairInfo`": "'KeyPairInfo'",
    ":py:class:`iam.InstanceProfile`": "'InstanceProfile'",
    ":py:class:`IAM.InstanceProfile`": "'InstanceProfile'",
    ":py:class:`IAM.AccessKey`": "'AccessKey'",
    ":py:class:`IAM.SamlProvider`": "'SamlProvider'",
    ":py:class:`iam.SamlProvider`": "'SamlProvider'",
    ":py:class:`EC2.Tag`": "'Tag'",
    ":py:class:`S3.BucketLifecycleConfiguration`": InternalImport(
        "BucketLifecycleConfiguration", "s3"
    ),
    ":py:class:`iam.AccountPasswordPolicy`": "'AccountPasswordPolicy'",
    ":py:class:`IAM.AccountPasswordPolicy`": "'AccountPasswordPolicy'",
    ":py:class:`S3.BucketNotification`": "'BucketNotification'",
    ":py:class:`CloudFormation.StackResource`": "'StackResource'",
    ":py:class:`EC2.Instance`": "'Instance'",
    ":py:class:`S3.BucketTagging`": "'BucketTagging'",
    ":py:class:`IAM.AccountSummary`": "'AccountSummary'",
    ":py:class:`EC2.Volume`": "'Volume'",
    ":py:class:`ec2.Volume`": "'Volume'",
    ":py:class:`SQS.Message`": "'Message'",
    ":py:class:`ec2.KeyPair`": "'KeyPair'",
    ":py:class:`S3.BucketAcl`": InternalImport("BucketAcl", "s3"),
    ":py:class:`S3.BucketRequestPayment`": InternalImport("BucketRequestPayment", "s3"),
    ":py:class:`IAM.Role`": "'Role'",
    ":py:class:`iam.Role`": "'Role'",
    ":py:class:`IAM.VirtualMfaDevice`": "'VirtualMfaDevice'",
    ":py:class:`iam.VirtualMfaDevice`": "'VirtualMfaDevice'",
    ":py:class:`Glacier.Account`": "'Account'",
    ":py:class:`S3.BucketLifecycle`": "'BucketLifecycle'",
    ":py:class:`EC2.DhcpOptions`": "'DhcpOptions'",
    ":py:class:`ec2.DhcpOptions`": "'DhcpOptions'",
    ":py:class:`S3.BucketLogging`": "'BucketLogging'",
    ":py:class:`Glacier.Notification`": "'Notification'",
    ":py:class:`EC2.ClassicAddress`": "'ClassicAddress'",
    ":py:class:`s3.Bucket`": InternalImport("Bucket", "s3"),
    ":py:class:`S3.Bucket`": InternalImport("Bucket", "s3"),
    ":py:class:`EC2.VpcAddress`": "'VpcAddress'",
    ":py:class:`S3.ObjectSummary`": InternalImport("ObjectSummary", "s3"),
    ":py:class:`EC2.NetworkInterfaceAssociation`": "'NetworkInterfaceAssociation'",
    ":py:class:`S3.ObjectAcl`": InternalImport("ObjectAcl", "s3"),
    "list(:py:class:`sns.PlatformApplication`)": "List['PlatformApplication']",
    "list(:py:class:`s3.ObjectSummary`)": AnnotationWrapper(
        parent=List, children=(InternalImport("ObjectSummary", "s3"),),
    ),
}