dataset_paths = {
	'celeba_train': '',
	'celeba_test': '',
	'celeba_train_4seg': '',
	'celeba_test_4seg': '',	
	'celeba_train_sketch': '',
	'celeba_test_sketch': '',
	'celeba_train_segmentation': '',
	'celeba_test_segmentation': '',
	'ffhq': '',
 	'mh_dataset' : '/kaggle/input/mh-dataset-seq-v4'
}

model_paths = {
	'stylegan_ffhq': 'pretrained_models/stylegan2-ffhq-config-f.pt',
	'ir_se50': 'pretrained_models/model_ir_se50.pth',
	'parsing_net': 'pretrained_models/parsing.pth',
	'circular_face': 'pretrained_models/CurricularFace_Backbone.pth',
	'mtcnn_pnet': 'pretrained_models/mtcnn/pnet.npy',
	'mtcnn_rnet': 'pretrained_models/mtcnn/rnet.npy',
	'mtcnn_onet': 'pretrained_models/mtcnn/onet.npy',
	'shape_predictor': 'pretrained_models/shape_predictor_68_face_landmarks.dat'
}
