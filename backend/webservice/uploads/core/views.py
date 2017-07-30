from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from uploads.core.models import Document
from uploads.core.forms import DocumentForm
import tensorflow as tf
import sys
import os

graph_file = "../Venomous_nonVenomous_inception.pb"
labels_txt = "../snake_labels.txt"



def home(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        image_path = "media/"+myfile.name
        image_data = tf.gfile.FastGFile(image_path, 'rb').read()
        label_lines = [line.rstrip() for line in tf.gfile.GFile(labels_txt)]

        with tf.gfile.FastGFile(graph_file, 'rb') as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())
            _ = tf.import_graph_def(graph_def, name='')
        with tf.Session() as sess:
            softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
            predictions = sess.run(softmax_tensor,{'DecodeJpeg/contents:0': image_data})
            top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
            temp = ['','']
            for node_id in top_k:
                human_string = label_lines[node_id]
                score = predictions[0][node_id]
                print(('%s (score = %.5f)' % (human_string, score)))
                if score>0.5:
                    scoree = str('%.2f' % (score*100))
                    stringg = str('%s' % (human_string))
        # return uploaded_file_url
        os.remove(image_path)
        return render(request, 'core/results.html', {
            'scoree': scoree,
            'stringg': stringg
        })

    return render(request, 'core/simple_upload.html')

