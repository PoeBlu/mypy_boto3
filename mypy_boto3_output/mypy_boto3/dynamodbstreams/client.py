from __future__ import annotations

# builtin imports
from typing import Dict
from typing import Any

# boto3 imports
from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def describe_stream(
        self, StreamArn: str, Limit: int = None, ExclusiveStartShardId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def generate_presigned_url(
        self,
        ClientMethod: str = None,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = None,
        HttpMethod: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_records(self, ShardIterator: str, Limit: int = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_shard_iterator(
        self,
        StreamArn: str,
        ShardId: str,
        ShardIteratorType: str,
        SequenceNumber: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_streams(
        self,
        TableName: str = None,
        Limit: int = None,
        ExclusiveStartStreamArn: str = None,
    ) -> Dict[str, Any]:
        pass