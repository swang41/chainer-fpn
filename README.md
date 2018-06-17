# Feature Pyramid Networks

1. Download pretrained model from [Detectron's model zoo](https://github.com/facebookresearch/Detectron/blob/master/MODEL_ZOO.md#end-to-end-faster--mask-r-cnn-baselines).
```
$ curl -L https://s3-us-west-2.amazonaws.com/detectron/35857345/12_2017_baselines/e2e_faster_rcnn_R-50-FPN_1x.yaml.01_36_30.cUF7QR7I/output/train/coco_2014_train%3Acoco_2014_valminusminival/generalized_rcnn/model_final.pkl -o e2e_faster_rcnn_R-50-FPN_1x.pkl
$ curl -L https://s3-us-west-2.amazonaws.com/detectron/35857890/12_2017_baselines/e2e_faster_rcnn_R-101-FPN_1x.yaml.01_38_50.sNxI7sX7/output/train/coco_2014_train%3Acoco_2014_valminusminival/generalized_rcnn/model_final.pkl -o e2e_faster_rcnn_R-101-FPN_1x.pkl
```

2. Convert weights.
```
$ python3 caffe22npz.py e2e_faster_rcnn_R-50-FPN_1x.pkl faster_rcnn_fpn_resnet50_coco.npz
```

3a. Run inference.
```
$ python3 demo.py [--gpu <gpu>] --model resnet50 faster_rcnn_fpn_resnet50_coco.npz <image>
```

3b. Run evalutation on MS COCO.
```
$ python3 eval_coco.py [--gpu <gpu>] --model resnet50 faster_rcnn_fpn_resnet50_coco.npz
```
