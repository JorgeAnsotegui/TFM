### YOLOv8

## Videos de las pruebas

- [YoloV8_n_fix.mp4](./YOLOv8/YoloV8_n_fix.mp4)
- [YoloV8_n_pre.mp4](./YOLOv8/YoloV8_n_pre.mp4)
- [YoloV8_n_all.mp4](./YOLOv8/YoloV8_n_all.mp4)
- [YoloV8_s_fix.mp4](./YOLOv8/YoloV8_s_fix.mp4)
- [YoloV8_s_pre.mp4](./YOLOv8/YoloV8_s_pre.mp4)
- [YoloV8_s_all.mp4](./YOLOv8/YoloV8_s_all.mp4)

## Métricas de los modelos usados en los videos

\[
\begin{array}{|l|c|c|c|c|c|c|}
\hline
\textbf{Métrica} & \multicolumn{3}{c|}{\textbf{Básico}} & \multicolumn{3}{c|}{\textbf{Preprocesado}} & \multicolumn{3}{c}{\textbf{\textit{Data Augmentation}}} \\
\cline{2-10}
 & \textbf{Nano} & \textbf{Pequeño} & & \textbf{Nano} & \textbf{Pequeño} & & \textbf{Nano} & \textbf{Pequeño} \\
\hline
\textbf{Recall}               & 0.88870 & 0.86150 & & 0.85538 & 0.86070 & & 0.90914 & 0.88452 \\
\textbf{Precisión}            & 0.91722 & 0.89066 & & 0.91621 & 0.81401 & & 0.88694 & 0.84628 \\
\textbf{IoU}                  & 0.82271 & 0.77910 & & 0.79333 & 0.71925 & & 0.81472 & 0.77038 \\
\textbf{F1 Score}             & 0.90273 & 0.87583 & & 0.88475 & 0.83670 & & 0.89790 & 0.83854 \\
\textbf{Inferencia (seg)}  & 0.01674 & 0.01739 & & 0.01231 & 0.01805 & & 0.01226 & 0.01541 \\
\hline
\end{array}
\]

### Detectron2

## Videos de las pruebas

- [Detectron2_n_fix.mp4](./Detectron2/Detectron2_n_fix.mp4)
- [Detectron2_n_pre.mp4](./Detectron2/Detectron2_n_pre.mp4)
- [Detectron2_n_all.mp4](./Detectron2/Detectron2_n_all.mp4)
- [Detectron2_s_fix.mp4](./Detectron2/Detectron2_s_fix.mp4)
- [Detectron2_s_pre.mp4](./Detectron2/Detectron2_s_pre.mp4)
- [Detectron2_s_all.mp4](./Detectron2/Detectron2_s_all.mp4)

## Métricas de los modelos usados en los videos

\[
\begin{array}{|l|c|c|c|c|c|c|}
\hline
\textbf{Métrica} & \multicolumn{2}{c|}{\textbf{Básico}} & \multicolumn{2}{c|}{\textbf{Preprocesado}} & \multicolumn{2}{c|}{\textbf{\textit{Data Augmentation}}} \\
\cline{2-7}
 & \textbf{Nano} & \textbf{Pequeño} & \textbf{Nano} & \textbf{Pequeño} & \textbf{Nano} & \textbf{Pequeño} \\
\hline
\textbf{Recall}               & 0.9041 & 0.8891 & 0.8441 & 0.8614 & 0.8906 & 0.8931 \\
\textbf{Precisión}            & 0.9148 & 0.8949 & 0.9047 & 0.8787 & 0.9083 & 0.9016 \\
\textbf{IoU}                  & 0.8338 & 0.8051 & 0.7752 & 0.7698 & 0.8171 & 0.8138 \\
\textbf{F1 Score}             & 0.9094 & 0.8920 & 0.8734 & 0.8699 & 0.8993 & 0.8973 \\
\textbf{Inferencia (seg)}     & 0.0452 & 0.0454 & 0.0354 & 0.0355 & 0.0352 & 0.0356 \\
\hline
\end{array}
\]