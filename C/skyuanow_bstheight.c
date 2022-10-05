int TreeHeight (Tree t) {
	
	if (t == NULL) {return 0;}
	if (t->left == NULL && t->right == NULL) {
		return 0;
	}

	int lh = TreeHeight(t->left);
	int rh = TreeHeight(t->right);

	int diff = lh - rh;

	if (lh > rh) {return 1 + lh}
	else {return rh + 1}
}
