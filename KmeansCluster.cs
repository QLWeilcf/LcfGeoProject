using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

namespace WinFormWithEcharts {
    class KmeansCluster {
        int _N;    //
        int _K;    //
        private float[][] _centroids;
        private float[][] _ctsCopy;
        private bool cv = false;
        public KmeansCluster () {
            _N = 2;
            _K = 3;
        }
        public KmeansCluster (int n, int k) {
            _N = n;
            _K = k;
        }


        private List<float[]> allDlst = new List<float[]>();//为省内存不用double

        public void loadData (string filenm) {
            //目前只针对二维的，想改进，之后再说吧
            StreamReader csvRder = new StreamReader(filenm);
            string csvall = csvRder.ReadToEnd();
            string[] csvlst = csvall.Split('\n');
            foreach (string c in csvlst) {
                string[] curLine = c.Split(',');
                if (curLine.Length == 2) {
                    float[] cline = new float[] {0f,0f,0f };
                    cline[0] =Convert.ToSingle( curLine[0]);
                    cline[1] = Convert.ToSingle(curLine[1]);
                    allDlst.Add(cline);
                }
                else {
                    Console.WriteLine(curLine.Length);
                }
                
            }

        }

        public float distEclud (float[] va, float[] vb) {
            //要求va vb里面元素个数相等
            if (va.Length != vb.Length) {
                throw new FormatException("va.Length 需要等于 vb.Length");
            }
            double sc = 0;
            for(int i = 0; i < va.Length; i++) {
                sc = sc + Math.Pow((va[i] - vb[i]), 2);
            }
            return (float)Math.Sqrt(sc);
        }

        public float[][] rand_center (List<float[]> data, int k) {
            //输出为k*n的矩阵；也可以用List<float[]>装，n指原先维数，默认为2
            int n = data[0].Length;
            float[][] centroids = new float[k][]; //这里填k而不是填n没问题
            for (int q = 0; q < k; q++) {
                centroids[q] = new float[] { 0, 0, 0 };
                }
            for (int i = 0; i < n; i++) {
                float _max = data[0][i];//or float.MinValue;//
                float _min= data[0][i];//循环一次可以获得最大最小值
                for(int j = 1; j < data.Count; j++) {
                    if (data[j][i] > _max) {
                        _max = data[j][i];
                    }
                    if (data[j][i] < _min) {
                        _min = data[j][i];
                    }
                }

                for (int q = 0; q < k; q++) {
                    var seed = Guid.NewGuid().GetHashCode();
                    Random ran = new Random(seed);//必须设置随机数种子，否则centroids相同
                    float rfloat = (float)ran.NextDouble();
                    centroids[q][i] =_min+(_max - _min)*rfloat;
                }
                
            }

            return centroids;
        }
        public bool converged (float[][] c1, float[][] c2) {
            //centroids not changed -> true
            for (int j = 0; j < c1.Length; j++) { //k
                for (int i = 0; i < c1[0].Length; i++) {// n
                    double a2 = Math.Abs(c1[j][i] - c2[j][i]);//这一句之后去优化
                    if (a2>0.0001) {
                        return false;
                    }
                }
            }
            return true;
        }
        /// <summary>
        /// 更新质心
        /// </summary>
        /// <returns></returns>
        private void updateCentroids () {
           for (int i = 0; i < _K; i++) {
                
            }
        }

        private float meanByAxis2 (int axis,float typec) {
            double msun = 0;
            int mc = 0;
            foreach(float[] a in allDlst) {
                if (a[_N - 1] == typec) {
                    msun = msun + a[axis];//这里特别怕溢出
                    mc += 1;
                }
            }
            return (float) msun /mc;
        }

        private float meanByAxis (int axis, float typec) {
            double mavg = 0;
            int mc = 0;
            foreach (float[] a in allDlst) {
                if (a[_N - 1] == typec) {
                    mc += 1;
                    mavg = mavg + (a[axis]-mavg)/mc;//
                }
            }
            return (float) mavg;
        }
        private float[] meanAll (float typec) {
            float[] newCts = new float[_N];
            for (int j = 0; j < _N; j++) {
                newCts[j] = meanByAxis(j, typec);
            }
            return newCts;
        }

        public List<float[]> cluster () {
            string fn = "D:/python_works/testSet3.csv";
            loadData(fn);
            _centroids = rand_center(allDlst, _K);
            int ncount = allDlst.Count;//注意和维度 _N 区分
            //目前用不到 assement
            while (!cv) {
                _ctsCopy = _centroids;
                for (int i = 0; i < ncount; i++) {
                    float minDist = float.MaxValue;
                    int minIndex = -1;
                    for (int j = 0; j < _K; j++) {
                        float dist = distEclud(allDlst[i], _centroids[j]);//注意j索引是否对
                        if (dist < minDist) {
                            minDist = dist;
                            minIndex = j;
                            allDlst[i][_N] = j;
                        }

                    }

                    
                }

                for (int q = 0; q < _K; q++) { // update centroid
                    _centroids[q] = meanAll(q);
                }
                cv = converged(_centroids, _ctsCopy);
            }
            return allDlst;
        }
        private string FloatLstToStr (float[] fl) {
            string otxt = "";
            foreach (float f in fl) {
                otxt = otxt + Convert.ToString(f) + ",";
            }
            return otxt;
        }

        public void toCluster () {
            List<float[]> allTwo = cluster();
            listFloatToCsv(allTwo);
        }
        //[lng,lat,flag] 写入csv
        public void listFloatToCsv (List<float[]> allT) {
            string spath = @"D:/python_works/testSet4_out.csv";
            StreamWriter swt = new StreamWriter(spath);
            foreach (float[] a in allT) {
                string outxt = FloatLstToStr(a);
                swt.WriteLine(outxt);
            }
            swt.Close();
        }

    }
}
