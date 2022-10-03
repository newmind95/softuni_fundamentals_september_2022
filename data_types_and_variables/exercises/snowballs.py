number_of_snowballs_made = int(input())

highest_calculated_snowball = 0
snowball_weight = 0
snowball_time = 0
snowball_quality = 0

for line in range(number_of_snowballs_made):
    weight_of_the_snowball = int(input())
    time_needed_to_hit_the_target = int(input())
    quality_of_snowball = int(input())
    snowball_value = (
            weight_of_the_snowball
            / time_needed_to_hit_the_target) ** quality_of_snowball
    if snowball_value > highest_calculated_snowball:
        highest_calculated_snowball = snowball_value
        snowball_weight = weight_of_the_snowball
        snowball_time = time_needed_to_hit_the_target
        snowball_quality = quality_of_snowball

print('%d : %d = %d (%d)' % (snowball_weight, snowball_time,
                             highest_calculated_snowball, snowball_quality))
