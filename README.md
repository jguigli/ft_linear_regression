# ft_linear_regression

[SUJET](https://cdn.intra.42.fr/pdf/pdf/117108/en.subject.pdf)  
[Regression lineaire avec Python](https://moncoachdata.com/blog/regression-lineaire-avec-python/)  
[Descente de gradient](https://www.ibm.com/fr-fr/topics/gradient-descent)  
[Regression lineaire](https://towardsdatascience.com/linear-regression-using-gradient-descent-97a6c8700931)  

[Youtube Modele lineaire](https://www.youtube.com/watch?v=wg7-roETbbM)  
[Youtube Modele lineaire](https://www.youtube.com/watch?v=8Y3r7F47Xfo)  

[Normalization](https://www.codecademy.com/article/normalization)  


# Command

In the directory /srcs :

	make

(Execute all commands in order)

	make train

Execute the training linear regression program based on csv data.

	make predict

Predict the price of a car according to the train model.

	make accuracy

Show the accuracy of the linear regression algorithm.

	make graph

Plot the data and the line resulting from the linear regression program

### Error GLib-GIO, lib use by GTK :

	(python:936105): GLib-GIO-CRITICAL : 13:04:52.622: g_dbus_connection_emit_signal: assertion 'object_path != NULL && g_variant_is_object_path (object_path)' failed
	(python:936105): GLib-GIO-CRITICAL : 13:04:52.645: g_dbus_connection_register_object: assertion 'object_path != NULL && g_variant_is_object_path (object_path)' failed

#### Solution 

Add in graph.py after import :

	matplotlib.use('TkAgg')
