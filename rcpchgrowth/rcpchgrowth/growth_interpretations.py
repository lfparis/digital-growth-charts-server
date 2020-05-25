

def interpret(measurement: str, centile: float, age: float):    
    """
    returns interpretations of centile values as string. Accepts age corrected if necessary
     - params: measurement (string, 'height', 'weight', 'ofc' 'bmi')
     - params: centile (float)
     - age: float (either a corrected or a chronological age)
    """
    
    lay_interpretation = ''
    clinician_interpretation = ''

    if measurement == 'height':
        if centile <= 0.04:
            if age < 2.0:
                lay_interpretation = "Your child has a lower or the same length as only 4 in every 1000 children the same age and sex. It is advisable to see your doctor."
            if age >= 2.0:
                lay_interpretation = "Your child has a lower or the same height as only 4 in every 1000 children the same age and sex. It is advisable to see your doctor."
            clinician_interpretation = "On or below the 0.04th centile for height. Medical review advised."
        elif centile <= 2.0:
            if age < 2.0:
                lay_interpretation = "Your child is in the lowest 2 percent for length, sex and age. Consider seeing your doctor."
            if age >= 2.0:
                lay_interpretation = "Your child is in the lowest 2 percent for height, sex and age. Consider seeing your doctor."
            clinician_interpretation = "On or below the 2nd centile. Consider reviewing trend."
        elif centile <= 9.0:
            if age < 2.0:
                lay_interpretation = "Your child is in the lowest 9 percent of the population for length, sex and age."
            elif age >= 2.0:
                lay_interpretation = "Your child is in the lowest 9 percent of the population for height, sex and age."
            clinician_interpretation = "On or below the 9th centile. Consider reviewing trend."
        elif centile <= 25.0:
            if age < 2.0:
                lay_interpretation = "Your child is in the lowest 1/4 of the population for length, sex and age."
            if age >= 2.0:
                lay_interpretation = "Your child is in the lowest 1/4 of the population for length, sex and age."
            clinician_interpretation = "On or below the 25th centile. Consider reviewing trend."
        elif centile <= 50.0:
            if age < 2.0:
                lay_interpretation = "Your child is on or just below the average length of the population for sex and age."
            if age >= 2.0:
                lay_interpretation = "Your child is on or just below the average height of the population for sex and age."
            clinician_interpretation = "On or below the 50th centile."
        elif centile <= 75.0:
            if age < 2.0:
                lay_interpretation = "Your child has the same or a shorter length than 75 percent of children the same age and sex."
            if age >= 2.0:
                lay_interpretation = "Your child has the same or a shorter height than 75 percent of children the same age and sex."
            clinician_interpretation = "On or below the 75th centile. Consider reviewing trend."
        elif centile <= 91.0:
            if age < 2.0:
                lay_interpretation = "Your child is in the top 9 percent of children the same age and sex for their length."
            if age >= 2.0:
                lay_interpretation = "Your child is in the top 9 percent of children the same age and sex for their height."
            clinician_interpretation = "On or below the 91st centile. Consider reviewing trend."
        elif centile <= 98.0:
            if age < 2.0:
                lay_interpretation = "Your child is in the top 2 percent of children the same age and sex for their length."
            if age >= 2.0:
                lay_interpretation = "Your child is in the top 2 percent of children the same age and sex for their length."
            clinician_interpretation = "On or below the 91st centile. Consider reviewing trend."
        elif centile <= 99.6:
            if age < 2.0:
                lay_interpretation = "Your child is longer than only 4 children in every 1000 the same age and sex. Consider seeking medical review."
            if age >= 2.0:
                lay_interpretation = "Your child is taller than only 4 children in every 1000 the same age and sex. Consider seeking medical review."
            clinician_interpretation = "On or below the 99.6th centile. Consider medical review."

    if measurement == 'weight':
        if centile <= 0.04:
            lay_interpretation = "Your child has a lower or the same weight as only 4 in every 1000 children the same age and sex. It is advisable to see your doctor."
            clinician_interpretation = "On or below the 0.04th centile for weight. Medical review advised."
        elif centile <= 2.0:
            lay_interpretation = "Your child is in the lowest 2 percent for weight compared with other children the same age and sex. Consider seeing your doctor."
            clinician_interpretation = "On or below the 2nd centile. Consider reviewing trend."
        elif centile <= 9.0:
            lay_interpretation = "Your child is in the lowest 9 percent of the population for weight compared with other children the same age and sex."
            clinician_interpretation = "On or below the 9th centile. Consider reviewing trend."
        elif centile <= 25.0:
            lay_interpretation = "Your child is in the lowest 1/4 of the population for weight, compared with other children the same age and sex."
            clinician_interpretation = "On or below the 25th centile. Consider reviewing trend."
        elif centile <= 50.0:
            lay_interpretation = "Your child is on or just below the average weight of the population, compared with other children the same age and sex."
            clinician_interpretation = "On or below the 50th centile ."
        elif centile <= 75.0:
            lay_interpretation = "Your child is below or the same as 75 percent of children the same age and sex. This does not take account of their height."
            clinician_interpretation = "On or below the 75th centile. Consider reviewing trend."
        elif centile <= 91.0:
            lay_interpretation = "Your child is in the top 9 percent of children the same age and sex for their weight. This does not take account of their height."
            clinician_interpretation = "On or below the 91st centile. Consider reviewing trend."
        elif centile <= 98.0:
            lay_interpretation = "Your child is in the top 2 percent of children the same age and sex for their weight. This does not take account of their height. Consider seeking medical review ."
            clinician_interpretation = "On or below the 91st centile. Consider reviewing trend."
        elif centile <= 99.6:
            lay_interpretation = "Your child is taller than only 4 children in every 1000 the same age and sex. This does not take account of their height. Medical review is advised."
            clinician_interpretation = "On or below the 99.6th centile. Consider medical review."

    if measurement == 'bmi':
        if centile:
            if centile <= 0.04:
                lay_interpretation = "Compared with other children the same height, age and sex, your child is below or the same weight as only 4 in every 1000 children. It is advisable to see your doctor."
                clinician_interpretation = "On or below the 0.04th centile. Medical review advised."
            elif centile <= 2.0:
                lay_interpretation = "Compared with other children the same height, age and sex, your child is is in the lowest 2 percent of the population for their weight. Consider seeing your doctor."
                clinician_interpretation = "On or below the 2nd centile. Consider reviewing trend."            
            elif centile <= 9.0:
                lay_interpretation = "Compared with other children the same height, age and sex, your child is in the lowest 9 percent of the population for weight."
                clinician_interpretation = "On or below the 9th centile. Consider reviewing trend."
            elif centile <= 25.0:
                lay_interpretation = "Compared with other children the same height, age and sex, your child is in the lowest 1/4 of the population for their weight."
                clinician_interpretation = "On or below the 25th centile. Consider reviewing trend."
            elif centile <= 50.0:
                lay_interpretation = "Compared with other children the same height, age and sex, your child is on or just below the average weight for the population ."
                clinician_interpretation = "On or below the 50th centile ."
            elif centile <= 75.0:
                lay_interpretation = "Compared with other children the same height, age and sex, your child is below or the same as 75 percent of children for their weight."
                clinician_interpretation = "On or below the 75th centile. Consider reviewing trend."
            elif centile <= 91.0:
                lay_interpretation = "Compared with other children the same height, age and sex, your child is in the top 9 percent of children for their weight."
                clinician_interpretation = "On or below the 91st centile. Consider reviewing trend."
            elif centile <= 98.0:
                lay_interpretation = "Compared with other children the same height, age and sex, your child is in the top 2 percent of children for their weight. Consider seeing your doctor."
                clinician_interpretation = "On or below the 98th centile. Meets definition for being overweight. Consider reviewing trend."
            elif centile <= 99.6:
                lay_interpretation = "Compared with other children the same height, age and sex, your child's  weight is lower than only 4 children in every 1000 childre. Medical review is advised."
                clinician_interpretation = "On or below the 99.6th centile. Above obesity threshold. Consider medical review."
        else:
            lay_interpretation = "BMI is not interpretable below 2 weeks of age"
            clinician_interpretation = 'There is no reference data below 2 weeks of age'

    if measurement == 'ofc':
        if centile <= 0.04:
            lay_interpretation = "Your child's head size is larger than or the same as only 4 in every 1000 children the same age and sex. It is advisable to see your doctor."
            clinician_interpretation = "On or below the 0.04th centile for head circumference. Medical review advised."
        elif centile <= 2.0:
            lay_interpretation = "Your child's head size is in the lowest 2 percent as other children the same sex and age. Consider seeing your doctor."
            clinician_interpretation = "On or below the 2nd centile for head circumference. Consider reviewing trend."
        elif centile <= 9.0:
            lay_interpretation = "Your child's head size is in the lowest 9 percent of the population for children the same sex and age."
            clinician_interpretation = "On or below the 9th centile for head circumference. Consider reviewing trend."
        elif centile <= 25.0:
            lay_interpretation = "Your child's head size is in the lowest 1/4 of the population compared with other children the same sex and age."
            clinician_interpretation = "On or below the 25th centile for head circumference. Consider reviewing trend."
        elif centile <= 50.0:
            lay_interpretation = "Your child is on or just below the average height of the population for sex and age."
            clinician_interpretation = "On or below the 50th centile for head circumference."
        elif centile <= 75.0:
            lay_interpretation = "Your child's head circumference is in the top 25 percent of children the same age and sex."
            clinician_interpretation = "On or below the 75th centile for head circumference. Consider reviewing trend."
        elif centile <= 91.0:
            lay_interpretation = "Your child's head circumference is in the top 9 percent of children the same age and sex."
            clinician_interpretation = "On or below the 91st centile for head circumference. Consider reviewing trend."
        elif centile <= 98.0:
            lay_interpretation = "Your child's head circumference is in the top 2 percent of children the same age and sex. Consider seeing your doctor."
            clinician_interpretation = "On or below the 91st centile for head circumference. Consider reviewing trend."
        elif centile <= 99.6:
            lay_interpretation = "Your child's head circumference is larger than only 4 children in every 1000 children the same age and sex. Medical review is advised."
            clinician_interpretation = "On or below the 99.6th centile for head circumference. Medical review is advised."

    return_comment =  {
        'clinician_comment': clinician_interpretation,
        'lay_comment': lay_interpretation
    }

    return return_comment

def comment_prematurity_correction(chronological_decimal_age, corrected_decimal_age, gestation_weeks, gestation_days):
    """
    Return interpretations on age correction as a string
    :Params - chronological_decimal_age : float
    :Params - corrected_decimal_age : float
    :Params - gestation_weeks : int
    :Params - gestation_days : int
    """
    if chronological_decimal_age == corrected_decimal_age:
        if gestation_weeks < 37 and gestation_weeks >= 32:
            lay_decimal_age_comment =   "Your child is now old enough nolonger to need to take their prematurity into account when considering their growth ."
            clinician_decimal_age_comment =  "Correction for gestational age is nolonger necessary after a year of age."
        if gestation_weeks < 33:
            lay_decimal_age_comment =   "Your child is now old enough nolonger to need to take their prematurity into account when considering their growth ."
            clinician_decimal_age_comment = "Correction for gestational age is nolonger necessary after two years of age."
    else:
        lay_decimal_age_comment =   "Your child's prematurity has been accounted for when considering their growth ."
        clinician_decimal_age_comment =  "Correction for gestational age has been made ."
    comment = {
        'lay_comment': lay_decimal_age_comment,
        'clinician_comment': clinician_decimal_age_comment
    }
    return comment