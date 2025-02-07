import trainer
import tester
import utils

experiences_list = trainer.get_epochs_data_list(
    ['./data_acquisition/subject7/subject7-1/record-bv-generic-nati-[2019.04.27-19.11.05].vhdr'])

train_experiences = experiences_list[:3]
test_experiences = experiences_list[3:]

classifier = trainer.train_classifier(train_experiences, './classifiers/subject7.joblib')
classification = tester.test_classifier(classifier, test_experiences)

state_files = ['./data_acquisition/subject7/subject7-1/grid_lights_experiment_nati_4',
               './data_acquisition/subject7/subject7-1/grid_lights_experiment_nati_5']

utils.merge_predictions_with_states(classification, state_files, utils.grid_lights_rewards, './rewards/subject7.txt')
