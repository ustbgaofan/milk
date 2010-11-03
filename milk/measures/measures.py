# -*- coding: utf-8 -*-
# Copyright (C) 2008-2010, Luis Pedro Coelho <lpc@cmu.edu>
# vim: set ts=4 sts=4 sw=4 expandtab smartindent:
# 
# License: MIT

from __future__ import division
import numpy
import numpy as np

__all__ = [
    'accuracy',
    'confusion_matrix',
    'waccuracy',
    'zero_one_loss',
    ]

def accuracy(real, other=None, normalisedlabels=False, names=None):
    '''
    acc = accuracy(real, predicted, normalisedlabels=False, names=None)

    Compute accuracy (fraction of correct predictions).

    Parameters
    ----------
    real : sequence
        The real labels
    predicted : sequence
        The predicted sequence (must be same type as `real`)
    normalisedlabels : boolean, optional
        Whether labels have been normalised
    names : sequence
        The underlying names (unused)

    Returns
    -------
    acc : float
    '''
    if other is None:
        import warnings
        warnings.warn(DeprecationWarning, 'milk.measures.accuracy: calling this with one argument is a deprecated interface.')
        cmatrix = np.asanyarray(cmatrix)
        return cmatrix.trace()/cmatrix.sum()
    else:
        real = cmatrix
        return np.mean(np.asanyarray(real) != other)

def zero_one_loss(real, predicted, normalisedlabels=False, names=None):
    '''
    loss = zero_one_loss(real, predicted, normalisedlabels={unused}, names={unused})

    Parameters
    ----------
    real : sequence
        the underlying labels
    predicted : sequence
        the predicted labels
    normalisedlabels : unused
    names: unused

    Returns
    -------
    loss : integer
        the number of instances where `real` differs from `predicted`
    '''
    return np.sum(np.asanyarray(real) != np.asanyarray(predicted))
    

def waccuracy(cmatrix):
    '''
    wacc = waccuracy(cmatrix)

    Weighted accuracy of cmatrix
    '''
    cmatrix = numpy.asanyarray(cmatrix)
    return (cmatrix.diagonal() / cmatrix.sum(1)).mean()

def confusion_matrix(real, predicted, normalisedlabels=False, names=None):
    '''
    cmatrix = confusion_matrix(real, predicted, normalisedlabels=False, names=None)

    Computes the confusion matrix

    Parameters
    ----------
    real : sequence
        The real labels
    predicted : sequence
        The predicted sequence (must be same type as `real`)
    normalisedlabels : boolean, optional
        Whether labels have been normalised
    names : sequence
        The underlying names (unused)

    Returns
    -------
    cmatrix : 2 ndarray
    '''
    if not normalisedlabels:
        from ..supervised.normalise import normaliselabels
        real, names = normaliselabels(real)
        predicted = map(names.index, predicted)
    n = np.max(real)+1
    cmat = np.zeros((n,n), int)
    for r,p in zip(real, predicted):
        cmat[r,p] += 1
    return cmat



## TODO: Implement http://en.wikipedia.org/wiki/Matthews_Correlation_Coefficient


