variable "enable_autoscaling" {
    description = "If set to true, enable auto scaling"
}

resource "aws_cloudwatch_metric_alarm" "high_cpu_utilization" {
    alarm_name = "${var.cluster_name}-high-cpu-utilization"
    namespace = "AWS/EC2"
    metric_name = "CPUUtilization"
    dimensions = {
      AutoScalingGroupName = "${aws_autoscaling_group.example.name}"
    }

    comparison_operator = "GreaterThanThreshold"
    evaluation_periods = 1
    period = 400
    statistic = "Average"
    threshold = 88
    unit = "Percent"
}
