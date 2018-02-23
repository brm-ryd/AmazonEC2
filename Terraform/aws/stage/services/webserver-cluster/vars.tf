variable "enable_autoscaling" {
  description = "if set TRUE, will enabled autoscaling"
}

resource "aws_autoscaling_schedule" "scale_out_business_hours" {
    count = "${var.enable_autoscaling}"

    scheduled_action_name = "scaleout-businesshours"
    min_size = 2
    max_size = 10
    desired_capacity = 10
    recurrence = "0 9 * * *"
    autoscaling_group_name = "${aws_autoscaling_group.webserver-stg}"
}

resource "aws_autoscaling_schedule" "scale_in_night" {
    count = "${var.enable_autoscaling}"

    scheduled_action_name = "scalein-night"
    min_size = 2
    max_size = 10
    desired_capacity = 2
    recurrence = "0 7 * * *"
    autoscaling_group_name = "${aws_autoscaling_group.webserver-stg}"
}
