import aws_cdk as cdk

from constructs import Construct

from aws_cdk.aws_chatbot import SlackChannelConfiguration

from aws_cdk.aws_sns import Topic

from notification.constructs.slack import SlackWebhook

from typing import Any


class NotificationStack(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.aws_igvf_staging_channel: SlackChannelConfiguration = SlackChannelConfiguration(
            self,
            'AwsIgvfStagingChannel',
            slack_channel_configuration_name='aws-pankbase-staging',
            slack_workspace_id='T074YEUTZAR',
            slack_channel_id='C075Q5XRD0Q',
        )
        self.alarm_notification_topic = Topic(
            self,
            'AwsIgvfStagingChannelAlarmNotificationTopic',
        )
        self.aws_igvf_staging_channel.add_notification_topic(
            self.alarm_notification_topic
        )
        self.aws_igvf_staging_channel_slack_webhook: SlackWebhook = SlackWebhook(
            self,
            'AwsIgvfStagingSlackWebhook',
        )
