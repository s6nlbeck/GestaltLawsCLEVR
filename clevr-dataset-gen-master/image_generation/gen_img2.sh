#!/bin/bash


echo "Generate Images"

echo "Proxi"

/home/nils/blender-2.78c-linux-glibc219-x86_64/blender --background --python render_images.py -- --num_images 50 --use_gpu 1 --num_groups 0 --output_image_dir /home/nils/clevr-dataset-gen-master/output/images/group_proximity_script-new2-TEST-Reserve --output_scene_dir /home/nils/clevr-dataset-gen-master/output/images/group_proximity_script-new-scene2-TEST-Reserve --group_by_postition 1 --filename_prefix proxRE


echo "Simi"


/home/nils/blender-2.78c-linux-glibc219-x86_64/blender --background --python render_images.py -- --num_images 50 --use_gpu 1 --group_by_similarity 1 --output_image_dir /home/nils/clevr-dataset-gen-master/output/images/group_similarity_script-new2-TEST-Reserve --output_scene_dir /home/nils/clevr-dataset-gen-master/output/images/group_similarity_script-new-scene2-TEST-Reserve --filename_prefix simiRE




echo "Conti"
/home/nils/blender-2.78c-linux-glibc219-x86_64/blender --background --python render_images.py -- --num_images 50 --use_gpu 1 --group_by_continuity 1 --output_image_dir /home/nils/clevr-dataset-gen-master/output/images/group_continuity_script-new-TEST-Reserve --output_scene_dir /home/nils/clevr-dataset-gen-master/output/images/group_continuity_script-new-scene-TEST-Reserve --filename_prefix contRE







echo "Fertig"
