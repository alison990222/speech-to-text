# text-to-speach


文档   
https://shimo.im/docs/9ThCDkJ6g8yxcxwq



##### speaker diarization task: in this task we need to separate different speakers in an audio recording. We have tried the following two methods
- google speaker diarization API: we enable google Speech-To-Text cloud service to try separating different speakers, however, maybe because it's still in beta version, it didn't work out quite well.
(https://cloud.google.com/speech-to-text/docs/multiple-voices#speech_transcribe_diarization_beta-python)
- pyAudioAnalysis(appendix 1):  we downloaded the source code and tried to run the demo with pretrained model. The accuracy was about 70%. But in the end we decide not to adopt this method, cause with only 70% accuracy, we might lose quite a lot useful information in the conversation.
(https://github.com/tyiannak/pyAudioAnalysis/wiki/5.-Segmentation#speaker-diarization)
