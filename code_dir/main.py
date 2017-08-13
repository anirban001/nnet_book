import code_dir.network as nw
import code_dir.mnist_loader as mnist_loader

from sklearn import svm

def _learn_with_networks():
    training_data, validation_data, test_data = (
        mnist_loader.load_data_wrapper())
    net = nw.Network([784, 30, 10])
    net.SGD(training_data, 3, 10, 3.0, test_data=test_data)


def _learn_with_support_vector_machines():
    # About 10 minutes
    # 9435 of 10000 values correct.
    training_data, validation_data, test_data = mnist_loader.load_data()
    # train
    clf = svm.SVC()
    clf.fit(training_data[0], training_data[1])
    # test
    predictions = [int(a) for a in clf.predict(test_data[0])]
    num_correct = sum(int(a == y) for a, y in zip(predictions, test_data[1]))
    print "Baseline classifier using an SVM."
    print "%s of %s values correct." % (num_correct, len(test_data[1]))


def do_main():
    # _learn_with_support_vector_machines()
    _learn_with_networks()
