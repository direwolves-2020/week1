numbers = [2, 34, 12, 29, 38, 1, 12, 8, 2, 7, 29, 38, 8, 1, 2, 3, 5, 10, 12, 8, 34, 9,7,10]

def metric_calculator(numbers):
    """Calculates a set of metrics on a given list of numbers"""

    def average(num_list):
        """Calculates the average of the provided list of numbers"""
        return round(sum(num_list)/len(num_list), 2)

    def median(num_list):
        """Calculates the median"""
        sortd = sorted(num_list)
        index_mid = int(len(sortd)/2)

        if len(sortd)%2:
            return sortd[index_mid]
        else:
            return average([sortd[index_mid-1], sortd[index_mid]])


    def mode(num_list):
        """Calculates the mode of a provided list of numbers"""
        number_count = {}

        max_pair = ([0], 0)

        for num in num_list:
            if num in number_count:
                number_count[num] += 1
            else:
                number_count[num] = 1

            # Check if it's occurrance count is greater than the max
            if number_count[num] > max_pair[1]:
                # We've got a new max, start the max_pair[0] list afresh
                max_pair = ([num], number_count[num])
            elif number_count[num] == max_pair[1]:
                # We have a number who's count equals the max. append to max_pain[0]
                max_pair[0].append(num)

        return max_pair[0]        

    return (average(numbers), median(numbers), mode(numbers))


if __name__ == '__main__':
    assert metric_calculator(numbers) == (13.38,8.5,[2,12,8])


