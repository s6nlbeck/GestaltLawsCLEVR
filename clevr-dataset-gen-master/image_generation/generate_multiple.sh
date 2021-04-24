#!/bin/bash


echo "Generate Images"

/home/nils/blender-2.78c-linux-glibc219-x86_64/blender --background --python render_images.py -- --num_images 100 --use_gpu 1 --group_by_closure 1 --output_image_dir /home/nils/clevr-dataset-gen-master/output/images/group_closure_script

/home/nils/blender-2.78c-linux-glibc219-x86_64/blender --background --python render_images.py -- --num_images 100 --use_gpu 1 --group_by_good_figure 1 --output_image_dir /home/nils/clevr-dataset-gen-master/output/images/group_good_figure_script

/home/nils/blender-2.78c-linux-glibc219-x86_64/blender --background --python render_images.py -- --num_images 100 --use_gpu 1 --group_by_continuity 1 --output_image_dir /home/nils/clevr-dataset-gen-master/output/images/group_continuity_script

/home/nils/blender-2.78c-linux-glibc219-x86_64/blender --background --python render_images.py -- --num_images 100 --use_gpu 1 --group_by_similarity 1 --output_image_dir /home/nils/clevr-dataset-gen-master/output/images/group_similarity_script

/home/nils/blender-2.78c-linux-glibc219-x86_64/blender --background --python render_images.py -- --num_images 100 --use_gpu 1 --num_groups 0 --output_image_dir /home/nils/clevr-dataset-gen-master/output/images/group_proximity_script



echo "Fertig"
