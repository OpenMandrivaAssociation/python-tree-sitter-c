Name:		python-tree-sitter-c
Version:	0.24.2
Release:	1
Summary:	Tree-sitter c grammar (Python bindings)
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/tree-sitter-c
Source0:	https://files.pythonhosted.org/packages/a6/c9/3834f3d9278251aea7312274971bc4c45b17aec2490fd4b884d93bd7019a/tree_sitter_c-0.24.2.tar.gz
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	clang
Requires:	python%{pyver}dist(tree-sitter)

%description
Tree-sitter grammar for c, compiled from source. Used by
Aider's grep-ast repo-map.

%prep
%autosetup -n tree_sitter_c-0.24.2

%build

%install
export CC=clang
python -m pip install \
	--no-deps --no-build-isolation --no-compile \
	--root %{buildroot} --prefix %{_prefix} \
	.

%files
%doc README.md
%license LICENSE
%{python_sitearch}/tree_sitter_c*
