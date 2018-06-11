import argparse
import matplotlib.pyplot as plt

import chainer

import chainercv
from chainercv.datasets import coco_bbox_label_names
from chainercv import utils

from faster_rcnn_fpn import FasterRCNNFPNResNet101


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('model')
    parser.add_argument('image')
    args = parser.parse_args()

    model = FasterRCNNFPNResNet101(n_fg_class=len(coco_bbox_label_names))
    chainer.serializers.load_npz(args.model, model)

    img = utils.read_image(args.image)
    bboxes, labels, scores = model.predict([img])
    bbox = bboxes[0]
    label = labels[0]
    score = scores[0]

    chainercv.visualizations.vis_bbox(
        img, bbox, label, score, label_names=coco_bbox_label_names)
    plt.show()


if __name__ == '__main__':
    main()
