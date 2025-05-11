This is a Face recognition attendance system.

How to run:
1.Make two folders in the same directory as all the python files called "dataset" and "training" (this will store the sample of faces in dataset folder and trainer.xml in training folder)
2.Run dataset_maker.py (enter the id of user eg.1,2,3,4..)
3.Open create_csv and add name of the user in student_list corresponding to the id entered before (eg. if John scanned his face with id 1 then add John first in the student_list and so on..So "John" would be student_list[0])
4.Train the model by running training.py
5.Finally run recognizer.py!
