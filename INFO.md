# CascadeClassifierTrainning

Treinamento de CascadeClassifier para reconhecimento de objetos usando OpenCV
Imagens negativas são as principais, as imagens são sobrepostas sobre todas as negativas e é assim que ele treina
Sera pego todas as imagens positivas e faram o mesmo para treinar

Rodar os scripts em sequencia e depois rodar os comandos:

# Cria amostras:
D:\Programs\OpenCV\opencv\build\x64\vc14\bin\opencv_createsamples -img mask.jpg -bg bg.txt -info info/info.lst -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 1300

## Descricao
opencv_createsamples 
  -img <img positiva de referencia>
  -bg <txt com imgs negativas>
  -info info/info.lst //Output
  -maxxangle 0.5 //default
  -maxyangle 0.5 //default
  -maxzangle 0.5 //default
  -num 1300 //deve ser no min 90% das imagens

na pasta info esta a imagem de amostra(mask.jpg) sobreposta nas imagens negativas

# Gera o vetor positivo:
D:\Programs\OpenCV\opencv\build\x64\vc14\bin\opencv_createsamples -info info/info.lst -num 1300 -w 20 -h 20 -vec positives.vec

## Descricao
opencv_createsamples 
  -info (local do arquivo info.lst da etapa anterior)
  -num 1300 //deve ser o mesmo que na etapa anterior
  -w 20 //default
  -h 20 //default
  -vec positives.vec //Output

# Treina a IA de verdade
D:\Programs\OpenCV\opencv\build\x64\vc14\bin\opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 1200 -numNeg 650 -numStages 10 -w 20 -h 20

## Descricao
opencv_traincascade 
  -data data //output onde o cascade sera gerado(é uma pasta deve ser gerado manualmente)
  -vec positives.vec //gerado na etapa anterior
  -bg bg.txt //lista negativos
  -numPos 1300 //mesmo que a etapa anterior
  -numNeg 650 //metade do numPos
  -numStages 10 
  -w 20 //mesmo que a etapa anterior
  -h 20 //mesmo que a etapa anterior

# quando receber o erro
OpenCV Error: Bad argument (Can not get new positive sample. The most possible reason is insufficient count of samples in given vec-file.
mudar -numPos 1200

# video tutorial

https://www.youtube.com/watch?v=EFZ1B70FMc0