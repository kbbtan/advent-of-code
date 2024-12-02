"""
Contains solutions for Day 5 stars.
Run on Python 3.8.3.
"""
import re

INPUT_FILE = "input.txt"

def star_1():
    """ Solution for Star 1.
    """
    def helper(mapping_lst, file):
        """ This function helps to convert the input mappings into list variables to work with.
                mapping_lst: the corresponding list which stores mappings
                file: the file object we are reading from
        """
        # Read the first line of mappings and extract the variables using regex.
        line = file.readline()
        mapping_vars = re.findall(r"([0-9]+) ([0-9]+) ([0-9]+)", line)

        # While we are still finding mapping_vars (there are more mappings to read), continue
        # reading and extracting from more lines.
        while mapping_vars:
            # Convert variables to integers to work with later.
            int_mapping_vars = tuple(map(lambda var: int(var), mapping_vars[0]))
            mapping_lst.append(int_mapping_vars)

            # Continue reading the next line.
            line = file.readline()
            mapping_vars = re.findall(r"([0-9]+) ([0-9]+) ([0-9]+)", line)

        # Dummy read one line to skip the header line of the next category of mappings.
        line = file.readline()

    def helper2(source_lst, mapping_lst):
        """ This function helps to convert the source numbers into their destination numbers based on
            the mappings provided in mapping_lst.
                source: the list containing numbers in the source category
                mapping_lst: the corresponding list which stores the mapping from source to destination
        """
        destination_lst = []

        for item in source_lst:
            mapping_found = False

            for mapping in mapping_lst:
                # The source number falls into this mapping range and we use it to determine its destination number.
                if item >= mapping[1] and item < mapping[1] + mapping[2]:
                    destination_lst.append(item - mapping[1] + mapping[0])
                    mapping_found = True
                    break

            # If we have not found a mapping, the number remains the same.
            if not mapping_found:
                destination_lst.append(item)

        return destination_lst

    # Define the list variables to store seeds and our mappings between each category.
    seeds = []
    seed_to_soils = []
    soil_to_fertilizers = []
    fertilizer_to_waters = []
    water_to_lights = []
    light_to_temperatures = []
    temperature_to_humidities = []
    humidity_to_locations = []

    with open(INPUT_FILE) as file:
        # Extract the seeds we start with, converting them to integers.
        line = file.readline()
        seeds = re.findall(r"[0-9]+", line)
        seeds = list(map(lambda seed: int(seed), seeds))

        # Dummy read two lines to skip the blank line and the header line of the next category of mappings.
        line = file.readline()
        line = file.readline()
        
        # Extract mapping variables for each category.
        helper(seed_to_soils, file)
        helper(soil_to_fertilizers, file)
        helper(fertilizer_to_waters, file)
        helper(water_to_lights, file)
        helper(light_to_temperatures, file)
        helper(temperature_to_humidities, file)
        helper(humidity_to_locations, file)

        # Go through each mapping to convert the seeds to locations.
        soils = helper2(seeds, seed_to_soils)
        fertilizers = helper2(soils, soil_to_fertilizers)
        waters = helper2(fertilizers, fertilizer_to_waters)
        lights = helper2(waters, water_to_lights)
        temperatures = helper2(lights, light_to_temperatures)
        humidities = helper2(temperatures, temperature_to_humidities)
        locations = helper2(humidities, humidity_to_locations)

        # Return the lowest location number.
        return min(locations)

def star_2():
    """ Solution for Star 2.
    """
    def helper(mapping_lst, file):
        """ This function helps to convert the input mappings into list variables to work with.
                mapping_lst: the corresponding list which stores mappings
                file: the file object we are reading from
        """
        # Read the first line of mappings and extract the variables using regex.
        line = file.readline()
        mapping_vars = re.findall(r"([0-9]+) ([0-9]+) ([0-9]+)", line)

        # While we are still finding mapping_vars (there are more mappings to read), continue
        # reading and extracting from more lines.
        while mapping_vars:
            # Convert variables to integers to work with later.
            int_mapping_vars = tuple(map(lambda var: int(var), mapping_vars[0]))
            mapping_lst.append(int_mapping_vars)

            # Continue reading the next line.
            line = file.readline()
            mapping_vars = re.findall(r"([0-9]+) ([0-9]+) ([0-9]+)", line)

        # Dummy read one line to skip the header line of the next category of mappings.
        line = file.readline()

    def helper2(source_lst, mapping_lst):
        """ This function helps to convert the source numbers into their destination numbers based on
            the mappings provided in mapping_lst.
                source: the list containing numbers and their ranges in the source category
                mapping_lst: the corresponding list which stores the mapping from source to destination
        """
        destination_lst = []

        # While there are still source ranges to find mappings for.
        while source_lst:
            item = source_lst.pop()
            item_start = item[0]
            item_end = item[1]
            mapping_found = False

            for mapping in mapping_lst:
                mapping_start = mapping[1]
                mapping_end = mapping[1] + mapping[2] - 1
                mapping_shift = mapping[0] - mapping[1]

                # Mapping falls outside the entire source range.
                if mapping_start > item_end or mapping_end < item_start:
                    continue

                # Source range is split into 3. Map the middle subset and reevaluate the others.
                elif mapping_start > item_start and mapping_end < item_end:
                    destination_lst.append((mapping_start + mapping_shift, mapping_end + mapping_shift))
                    source_lst.append((item_start, mapping_start - 1))
                    source_lst.append((mapping_end + 1, item_end))
                    mapping_found = True
                    break

                # Source range is split into 2. Map the right subset and reevaluate the left subset.
                elif mapping_start > item_start:
                    destination_lst.append((mapping_start + mapping_shift, item_end + mapping_shift))
                    source_lst.append((item_start, mapping_start - 1))
                    mapping_found = True
                    break
                
                # Source range is split into 2. Map the left subset and reevaluate the left subset.
                elif mapping_end < item_end:
                    destination_lst.append((item_start + mapping_shift, mapping_end + mapping_shift))
                    source_lst.append((mapping_end + 1, item_end))
                    mapping_found = True
                    break

                # Mapping captures entire source range. Map the entire source range.
                else:
                    destination_lst.append((item_start + mapping_shift, item_end + mapping_shift))
                    mapping_found = True
                    break

            # If we have not found a mapping, the entire range remains the same.
            if not mapping_found:
                destination_lst.append(item)

        return destination_lst

    # Define the list variables to store seeds and our mappings between each category.
    seeds = []
    seed_to_soils = []
    soil_to_fertilizers = []
    fertilizer_to_waters = []
    water_to_lights = []
    light_to_temperatures = []
    temperature_to_humidities = []
    humidity_to_locations = []

    with open(INPUT_FILE) as file:
        # Extract the seeds we start with and their ranges.
        line = file.readline()
        seeds = re.findall(r"([0-9]+) ([0-9]+)", line)
        
        # Convert these ranges from (start, range) to (start, end) for processing.
        # Also convert them to integers.
        for i in range(len(seeds)):
            seeds[i] = (int(seeds[i][0]), int(seeds[i][0]) + int(seeds[i][1]) - 1)

        # Dummy read two lines to skip the blank line and the header line of the next category of mappings.
        line = file.readline()
        line = file.readline()
        
        # Extract mapping variables for each category.
        helper(seed_to_soils, file)
        helper(soil_to_fertilizers, file)
        helper(fertilizer_to_waters, file)
        helper(water_to_lights, file)
        helper(light_to_temperatures, file)
        helper(temperature_to_humidities, file)
        helper(humidity_to_locations, file)
        
        # Go through each mapping to convert the seeds to locations.
        soils = helper2(seeds, seed_to_soils)
        fertilizers = helper2(soils, soil_to_fertilizers)
        waters = helper2(fertilizers, fertilizer_to_waters)
        lights = helper2(waters, water_to_lights)
        temperatures = helper2(lights, light_to_temperatures)
        humidities = helper2(temperatures, temperature_to_humidities)
        locations = helper2(humidities, humidity_to_locations)

        # Return the lowest location number.
        return min(locations, key=lambda location: location[0])[0]

def main():
    """ Contains driver code for running solutions.
    """
    print("Solution for Star 1: ", star_1())
    print("Solution for Star 2: ", star_2())

main()