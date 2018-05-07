#! /bin/zsh

for ((i=900; i<1000; i=i+2)); do
	sudo pyfr export cylinder_2d.pyfrm cylinder_2d_${i}.00.pyfrs export/cylinder_2d_${i}.vtu 
done
