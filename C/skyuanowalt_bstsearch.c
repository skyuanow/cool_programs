TreeContains(Tree tree, Node key) {
	if tree == NULL {
		return false;
	} else if key->data < tree->data {
		return TreeContains(tree->left, key);
	} else if key->data > tree->data {
		return TreeContains(tree->right, key);
	} else {
		return true;
	}
}
