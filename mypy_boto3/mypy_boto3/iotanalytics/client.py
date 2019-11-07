from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def batch_put_message(
        self,
        channelName: str,
        messages: List,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def cancel_pipeline_reprocessing(
        self,
        pipelineName: str,
        reprocessingId: str,
    ) -> Dict:
        pass


    def create_channel(
        self,
        channelName: str,
        channelStorage: Optional[Dict] = None,
        retentionPeriod: Optional[Dict] = None,
        tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_dataset(
        self,
        datasetName: str,
        actions: List,
        triggers: Optional[List] = None,
        contentDeliveryRules: Optional[List] = None,
        retentionPeriod: Optional[Dict] = None,
        versioningConfiguration: Optional[Dict] = None,
        tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_dataset_content(
        self,
        datasetName: str,
    ) -> Dict:
        pass


    def create_datastore(
        self,
        datastoreName: str,
        datastoreStorage: Optional[Dict] = None,
        retentionPeriod: Optional[Dict] = None,
        tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_pipeline(
        self,
        pipelineName: str,
        pipelineActivities: List,
        tags: Optional[List] = None,
    ) -> Dict:
        pass


    def delete_channel(
        self,
        channelName: str,
    ):
        pass


    def delete_dataset(
        self,
        datasetName: str,
    ):
        pass


    def delete_dataset_content(
        self,
        datasetName: str,
        versionId: Optional[str] = None,
    ):
        pass


    def delete_datastore(
        self,
        datastoreName: str,
    ):
        pass


    def delete_pipeline(
        self,
        pipelineName: str,
    ):
        pass


    def describe_channel(
        self,
        channelName: str,
        includeStatistics: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_dataset(
        self,
        datasetName: str,
    ) -> Dict:
        pass


    def describe_datastore(
        self,
        datastoreName: str,
        includeStatistics: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_logging_options(
        self,
    ) -> Dict:
        pass


    def describe_pipeline(
        self,
        pipelineName: str,
    ) -> Dict:
        pass


    def generate_presigned_url(
        self,
        ClientMethod: Optional[str] = None,
        Params: Optional[Dict] = None,
        ExpiresIn: Optional[int] = None,
        HttpMethod: Optional[str] = None,
    ):
        pass


    def get_dataset_content(
        self,
        datasetName: str,
        versionId: Optional[str] = None,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_channels(
        self,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_dataset_contents(
        self,
        datasetName: str,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
        scheduledOnOrAfter: Optional[datetime] = None,
        scheduledBefore: Optional[datetime] = None,
    ) -> Dict:
        pass


    def list_datasets(
        self,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_datastores(
        self,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_pipelines(
        self,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        resourceArn: str,
    ) -> Dict:
        pass


    def put_logging_options(
        self,
        loggingOptions: Dict,
    ):
        pass


    def run_pipeline_activity(
        self,
        pipelineActivity: Dict,
        payloads: List,
    ) -> Dict:
        pass


    def sample_channel_data(
        self,
        channelName: str,
        maxMessages: Optional[int] = None,
        startTime: Optional[datetime] = None,
        endTime: Optional[datetime] = None,
    ) -> Dict:
        pass


    def start_pipeline_reprocessing(
        self,
        pipelineName: str,
        startTime: Optional[datetime] = None,
        endTime: Optional[datetime] = None,
    ) -> Dict:
        pass


    def tag_resource(
        self,
        resourceArn: str,
        tags: List,
    ) -> Dict:
        pass


    def untag_resource(
        self,
        resourceArn: str,
        tagKeys: List,
    ) -> Dict:
        pass


    def update_channel(
        self,
        channelName: str,
        channelStorage: Optional[Dict] = None,
        retentionPeriod: Optional[Dict] = None,
    ):
        pass


    def update_dataset(
        self,
        datasetName: str,
        actions: List,
        triggers: Optional[List] = None,
        contentDeliveryRules: Optional[List] = None,
        retentionPeriod: Optional[Dict] = None,
        versioningConfiguration: Optional[Dict] = None,
    ):
        pass


    def update_datastore(
        self,
        datastoreName: str,
        retentionPeriod: Optional[Dict] = None,
        datastoreStorage: Optional[Dict] = None,
    ):
        pass


    def update_pipeline(
        self,
        pipelineName: str,
        pipelineActivities: List,
    ):
        pass
