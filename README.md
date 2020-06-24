# Libsvm_cvo
Libsvm_cvo provided the predicted result during cross validation based on libsvm-3.22.


Usage: svm-train -v 5 [options] -b 1 test.scale


1.Download Libsvm_cvo at and prepare your data in scale format.

2. Type

    cd Libsvm_cvo && make clean && make

3. To get the result of cross validation.

//cross validation with probability_estimates

    ./svm-train -v 5 -b 1 test.scale

//cross validation without probability_estimates

    ./svm-train -v 5 -b 0 test.scale

4. Open cross_prob1.txt/cross_prob0.txt to get the result of cross validation.

