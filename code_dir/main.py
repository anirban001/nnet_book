import code_dir.network as nw
import code_dir.mnist_loader as mnist_loader

from sklearn import svm
import sys


def _visualize():
    training_data, validation_data, test_data = mnist_loader.load_data()
    for input_index in range(20):
        vec = training_data[0][input_index]
        print 'Expected = ', training_data[1][input_index]
        assert 784 == len(vec)
        index = -1
        for i in range(28):
            for j in range(28):
                index += 1
                pixel = '##' if vec[index] > 0.5  else '__'
                sys.stdout.write(pixel)
            print
        print


def _visualize1():
    training_data, validation_data, test_data = mnist_loader.load_data()
    print 'training_data   : ', mnist_loader.get_type(training_data)
    print 'validation_data : ', mnist_loader.get_type(validation_data)
    print 'test_data       : ', mnist_loader.get_type(test_data)


def _visualize2():
    training_data, validation_data, test_data = (
        mnist_loader.load_data_wrapper())
    print 'training_data   : ', mnist_loader.get_type(training_data)
    print 'validation_data : ', mnist_loader.get_type(validation_data)
    print 'test_data       : ', mnist_loader.get_type(test_data)


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
    # _learn_with_networks()
    # _learn_with_support_vector_machines()
    _visualize()
