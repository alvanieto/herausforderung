Feature: POI-Adquisition
    As a Data Scients I want the best POI data


Scenario Outline: Merging to csv files with different normalization alghoritm
    Given two files <input_data_1> and <input_data_2>
    When I merge these files with normalize alghoritm <alghoritm>
    Then I get the next merged file <merged_data>

    Examples:
    | input_data_1             | input_data_2             | alghoritm  | merged_data             |
    | input_data_no_norm_1.csv | input_data_no_norm_2.csv | None       | merged_data_no_norm.csv |
