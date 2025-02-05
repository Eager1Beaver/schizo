import torch
import torch.nn as nn
from torchvision import models
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

# ResNet-18 for Feature Extraction
class FeatureExtractor(nn.Module):
    def __init__(self, base_model_name='resnet18', weights=models.ResNet18_Weights.IMAGENET1K_V1, input_channels=1):
        super(FeatureExtractor, self).__init__()
        base_model = getattr(models, base_model_name)(weights=weights)
        # Remove the classification layer
        self.feature_extractor = nn.Sequential(*list(base_model.children())[:-1])

        # Modify the first convolutional layer
        conv1 = self.feature_extractor[0]
        self.feature_extractor[0] = nn.Conv2d(
            in_channels=input_channels,
            out_channels=conv1.out_channels,
            kernel_size=conv1.kernel_size,
            stride=conv1.stride,
            padding=conv1.padding,
            bias=conv1.bias
        )
        # Copy the weights from the first channel of the original conv1 layer
        self.feature_extractor[0].weight.data = conv1.weight.data.mean(dim=1, keepdim=True)

    def forward(self, x):
        x = self.feature_extractor(x)
        return x.view(x.size(0), -1)  # Flatten to (batch_size, feature_dim)
    
# Support Vector Classifier for image classification
class SVMClassifier:
    def __init__(self, kernel='rbf', C=100, gamma=0.0001, random_state=42):
        """Initializes the SVM classifier with specified parameters."""
        self.pipeline = make_pipeline(
            StandardScaler(),
            SVC(kernel=kernel, probability=True, C=C, gamma=gamma, random_state=random_state)
        )
    
    def train(self, train_features, train_labels):
        """Trains the SVM classifier on the given data."""
        self.pipeline.fit(train_features, train_labels)
    
    def predict(self, test_features):
        """Predicts labels for the given test features."""
        return self.pipeline.predict(test_features)
    
    def predict_proba(self, test_features):
        """Returns probability estimates for the given test features."""
        return self.pipeline.predict_proba(test_features)