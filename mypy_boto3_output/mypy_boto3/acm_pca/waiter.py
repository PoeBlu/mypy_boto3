from __future__ import annotations

# builtin imports
from typing import Dict
from typing import Any

# boto3 imports
from botocore.waiter import Waiter


class AuditReportCreated(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        CertificateAuthorityArn: str,
        AuditReportId: str,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class CertificateAuthorityCSRCreated(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self, CertificateAuthorityArn: str, WaiterConfig: Dict[str, Any] = None
    ) -> None:
        pass


class CertificateIssued(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        CertificateAuthorityArn: str,
        CertificateArn: str,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass