---
class: note
tags:
  - y3s2
  - python
  - matplotlib
source:
related:
author:
date: 2026-03-11
updated: 2026-03-11 03:36:09
aliases:
---
# Matplotlib Comprehensive Reference

Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. It's the foundational plotting library that pandas and other packages build on.

## QUICK REFERENCE

### Most Common Functions


```python
# Creating plots
plt.plot(), plt.scatter(), plt.hist(), plt.bar(), plt.boxplot()

# Customization
plt.xlabel(), plt.ylabel(), plt.title(), plt.legend(), plt.grid()

# Limits and ticks
plt.xlim(), plt.ylim(), plt.xticks(), plt.yticks()

# Subplots
plt.subplots(), plt.subplot()

# Adding elements
plt.axhline(), plt.axvline(), plt.text(), plt.annotate()

# Saving
plt.savefig(), plt.tight_layout()

# Display
plt.show(), plt.close()
```

### Figure vs Axes Methods


```python
# These are equivalent:
plt.xlabel('X')           # pyplot interface
ax.set_xlabel('X')        # object-oriented

plt.title('Title')        # pyplot
ax.set_title('Title')     # OO

plt.xlim(0, 10)           # pyplot
ax.set_xlim(0, 10)        # OO
```

**Recommendation:** Use object-oriented interface (ax.) for better control, especially with multiple subplots!

---

## IMPORTING


```python
import matplotlib.pyplot as plt
import numpy as np
```

**Standard workflow:**

1. Create figure and axes
2. Plot data
3. Customize (labels, title, etc.)
4. Display or save

---

## BASIC PLOT TYPES

### Line Plot


```python
plt.plot(x, y)                         # basic line plot
plt.plot(x, y, 'r-')                   # red solid line
plt.plot(x, y, 'b--')                  # blue dashed line
plt.plot(x, y, 'go')                   # green circles
plt.plot(x, y, label='Data')           # with label for legend
```

### Scatter Plot


```python
plt.scatter(x, y)                      # basic scatter
plt.scatter(x, y, c='red', s=50)       # red, size 50
plt.scatter(x, y, c=colors, s=sizes)   # variable color and size
plt.scatter(x, y, alpha=0.5)           # 50% transparent
```

### Histogram


```python
plt.hist(data, bins=20)                # 20 bins
plt.hist(data, bins=20, edgecolor='black')  # with bin edges
plt.hist(data, bins=20, density=True)  # normalized (density)
plt.hist(data, bins=[0, 10, 20, 30])   # custom bin edges
```

**From lectures:**


```python
# Histogram convention: left-closed intervals [a, b)
# Last bin is closed on both ends [a, b]
# DIFFERENT from R which uses right-closed (a, b]
```

### Bar Chart


```python
plt.bar(x, height)                     # vertical bars
plt.barh(y, width)                     # horizontal bars
plt.bar(x, height, width=0.8)          # bar width
plt.bar(x, height, color='steelblue')  # color
```

### Box Plot


```python
plt.boxplot(data)                      # single box plot
plt.boxplot([data1, data2, data3])     # multiple boxes
plt.boxplot(data, vert=False)          # horizontal
plt.boxplot(data, showmeans=True)      # show mean marker
```

---

## FIGURE AND AXES

### Single Plot


```python
# Simple way (implicit)
plt.plot(x, y)
plt.show()

# Explicit way (recommended)
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
```

### Multiple Subplots


```python
# Grid of subplots
fig, axes = plt.subplots(2, 3, figsize=(12, 8))  # 2 rows, 3 cols
# axes is 2D array: axes[row, col]

# Example: 1 row, 3 columns
fig, axes = plt.subplots(1, 3, figsize=(12, 4))
axes[0].plot(x, y1)
axes[1].hist(data)
axes[2].scatter(x, y2)

# Share x or y axis
fig, axes = plt.subplots(2, 1, sharex=True)
```

**From Tutorial 3:**


```python
# Creating panel density plots manually
fig, axes = plt.subplots(1, 3, figsize=(12, 4))
for i, (group_name, group_df) in enumerate(df.groupby('category')):
    axes[i].hist(group_df['value'], bins=20)
    axes[i].set_title(group_name)
```

---

## CUSTOMIZATION

### Labels and Titles


```python
plt.xlabel('X-axis label', fontsize=12)
plt.ylabel('Y-axis label', fontsize=12)
plt.title('Plot Title', fontsize=14, fontweight='bold')

# Using axes object
ax.set_xlabel('X-axis label', fontsize=12)
ax.set_ylabel('Y-axis label', fontsize=12)
ax.set_title('Plot Title', fontsize=14)
```

### Axis Limits and Ticks


```python
plt.xlim(0, 10)                        # x-axis limits
plt.ylim(-5, 5)                        # y-axis limits
plt.xticks([0, 2, 4, 6, 8, 10])        # custom x-ticks
plt.yticks(np.arange(-5, 6, 1))        # y-ticks with range
plt.xticks([])                         # hide x-ticks
```

### Grid


```python
plt.grid(True)                         # add grid
plt.grid(True, alpha=0.3)              # transparent grid
plt.grid(True, linestyle='--')         # dashed grid
plt.grid(True, which='both')           # major and minor
```

### Legend


```python
plt.legend()                           # automatic from labels
plt.legend(['Line 1', 'Line 2'])       # manual labels
plt.legend(loc='upper right')          # position
plt.legend(loc='best')                 # auto position
plt.legend(frameon=False)              # no box around legend
```

**Common legend positions:**

- `'upper right'`, `'upper left'`
- `'lower right'`, `'lower left'`
- `'center'`, `'best'`

---

## COLORS AND STYLES

### Color Specification


```python
# Named colors
plt.plot(x, y, color='red')
plt.plot(x, y, color='steelblue')

# Hex colors
plt.plot(x, y, color='#FF5733')

# RGB tuples (0-1 scale)
plt.plot(x, y, color=(0.2, 0.4, 0.6))

# RGBA with transparency
plt.plot(x, y, color=(1, 0, 0, 0.5))   # 50% transparent red
```

**From lectures - Transparency for overplotting:**


```python
# RGB with alpha channel
red_transparent = (1, 0, 0, 0.25)      # 25% opaque
plt.scatter(x, y, c=red_transparent, s=50)
```

### Line Styles


```python
plt.plot(x, y, linestyle='-')          # solid (default)
plt.plot(x, y, linestyle='--')         # dashed
plt.plot(x, y, linestyle='-.')         # dash-dot
plt.plot(x, y, linestyle=':')          # dotted
plt.plot(x, y, linewidth=2)            # line width
```

### Marker Styles


```python
plt.plot(x, y, marker='o')             # circle
plt.plot(x, y, marker='s')             # square
plt.plot(x, y, marker='^')             # triangle up
plt.plot(x, y, marker='*')             # star
plt.plot(x, y, markersize=10)          # marker size
plt.plot(x, y, markerfacecolor='red')  # fill color
plt.plot(x, y, markeredgecolor='black')  # edge color
```

**Short format string:**


```python
plt.plot(x, y, 'ro-')                  # red circles with line
plt.plot(x, y, 'bs--')                 # blue squares, dashed
plt.plot(x, y, 'g^:')                  # green triangles, dotted
```

---

## ADDING ELEMENTS

### Text Annotations


```python
plt.text(x, y, 'Text here')            # add text at (x, y)
plt.text(x, y, 'Text', fontsize=12, ha='center', va='top')

# Annotate with arrow
plt.annotate('Peak', xy=(x, y), xytext=(x+1, y+1),
             arrowprops=dict(arrowstyle='->'))
```

**From assignment:** Adding text to plots


```python
ax.text(0.05, 0.95, 
        f'χ² = {chi2:.2f}, p < 0.001',
        transform=ax.transAxes,        # use axes coordinates (0-1)
        fontsize=11,
        verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
```

### Lines and Shapes


```python
plt.axhline(y=0, color='k', linestyle='--')  # horizontal line
plt.axvline(x=5, color='r', linestyle='-')   # vertical line
plt.axhline(y=0, xmin=0.2, xmax=0.8)         # partial line

# Add line from slope and intercept
plt.axline((x1, y1), (x2, y2))               # line through 2 points
plt.axline((x1, y1), slope=m)                # line with slope
```

**From lectures:**


```python
# Add regression line to scatter plot
plt.scatter(x, y)
plt.axline((x1, y1), slope=slope, color='red', linestyle='--')
```

### Rectangles and Patches


```python
from matplotlib.patches import Rectangle

rect = Rectangle((x, y), width, height, 
                 facecolor='blue', alpha=0.3)
ax.add_patch(rect)
```

---

## STYLING AND THEMES

### Style Sheets


```python
plt.style.use('default')               # default style
plt.style.use('seaborn-v0_8')          # seaborn style
plt.style.use('ggplot')                # ggplot style
plt.style.available                    # list all styles
```

### Figure Size and DPI


```python
plt.figure(figsize=(10, 6))            # width, height in inches
fig, ax = plt.subplots(figsize=(10, 6))

# For saving
plt.savefig('plot.png', dpi=300)       # high resolution
```

### Tight Layout


```python
plt.tight_layout()                     # auto-adjust spacing
# Prevents labels from being cut off
```

---

## SAVING FIGURES


```python
plt.savefig('plot.png')                # save as PNG
plt.savefig('plot.pdf')                # save as PDF
plt.savefig('plot.svg')                # save as SVG
plt.savefig('plot.png', dpi=300)       # high resolution
plt.savefig('plot.png', bbox_inches='tight')  # no whitespace
plt.savefig('plot.png', transparent=True)     # transparent background
```

---

## SPECIAL PLOT TYPES

### Heatmap (using imshow)


```python
# For matrix/2D data
plt.imshow(matrix, cmap='viridis')
plt.colorbar()                         # add color scale
plt.imshow(matrix, cmap='coolwarm', vmin=-1, vmax=1)  # symmetric

# Common colormaps
# Sequential: 'viridis', 'plasma', 'Blues', 'Reds'
# Diverging: 'coolwarm', 'RdBu', 'seismic'
# Qualitative: 'Set1', 'Set2', 'tab10'
```

**From lectures:** Correlation heatmaps


```python
# Must set vmin=-1, vmax=1 for correlation matrices
import seaborn as sns
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', 
            vmin=-1, vmax=1, center=0)
```

### Density/KDE Plot


```python
from scipy.stats import gaussian_kde

density = gaussian_kde(data)
x_range = np.linspace(data.min(), data.max(), 100)
plt.plot(x_range, density(x_range))
```

### Q-Q Plot


```python
from scipy import stats

stats.probplot(data, dist="norm", plot=plt)
plt.title('Q-Q Plot')
plt.show()
```

**From Exercise 4:**


```python
# Create Q-Q plot with customization
fig, ax = plt.subplots(figsize=(10, 8))
stats.probplot(residuals, dist="norm", plot=ax)

# Customize markers
ax.get_lines()[0].set_markerfacecolor('#e74c3c')
ax.get_lines()[0].set_markeredgecolor('black')
ax.get_lines()[0].set_markersize(12)

# Customize reference line
ax.get_lines()[1].set_color('#2c3e50')
ax.get_lines()[1].set_linewidth(2)
ax.get_lines()[1].set_linestyle('--')
```

---

## WORKING WITH PANDAS

### DataFrame Plotting


```python
# Pandas uses matplotlib backend
df.plot()                              # default line plot
df.plot(kind='scatter', x='col1', y='col2')
df.plot(kind='bar')
df.plot(kind='hist', bins=20)
df.plot(kind='box')

# Access underlying axes
ax = df.plot(kind='scatter', x='col1', y='col2')
ax.set_xlabel('Custom Label')
```

### Grouped Plotting


```python
# Plot by group
for name, group in df.groupby('category'):
    plt.scatter(group['x'], group['y'], label=name)
plt.legend()
```

---

## ADVANCED TECHNIQUES

### Subplots with Different Sizes


```python
# Using GridSpec
from matplotlib.gridspec import GridSpec

fig = plt.figure(figsize=(10, 8))
gs = GridSpec(3, 3, figure=fig)

ax1 = fig.add_subplot(gs[0, :])       # top row, all columns
ax2 = fig.add_subplot(gs[1, :-1])     # middle row, first 2 cols
ax3 = fig.add_subplot(gs[1:, -1])     # last 2 rows, last col
```

### Twin Axes (Two Y-axes)


```python
fig, ax1 = plt.subplots()

ax1.plot(x, y1, 'b-')
ax1.set_ylabel('Y1', color='b')

ax2 = ax1.twinx()                      # create second y-axis
ax2.plot(x, y2, 'r-')
ax2.set_ylabel('Y2', color='r')
```

### Log Scale


```python
plt.yscale('log')                      # log scale on y-axis
plt.xscale('log')                      # log scale on x-axis
plt.loglog()                           # log both axes
plt.semilogx()                         # log x only
plt.semilogy()                         # log y only
```

### Filling Between Curves


```python
plt.fill_between(x, y1, y2, alpha=0.3)  # fill between two curves
plt.fill_between(x, 0, y, alpha=0.5)    # fill from zero
```

---

## INTERACTIVE FEATURES

### Zoom and Pan


```python
# In Jupyter notebooks
%matplotlib notebook                   # interactive mode

# Or inline (static)
%matplotlib inline
```

### Closing Figures


```python
plt.close()                            # close current figure
plt.close('all')                       # close all figures
plt.close(fig)                         # close specific figure
```

---

## COMMON PATTERNS FROM COURSE

### Pattern 1: Basic Scatter with Regression Line


```python
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(x, y, alpha=0.6, edgecolors='black')
ax.axline((x1, y1), slope=slope, color='red', linestyle='--', label='Fit')
ax.set_xlabel('X variable')
ax.set_ylabel('Y variable')
ax.set_title('Scatter Plot with Regression Line')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('scatter_regression.png', dpi=300)
```

### Pattern 2: Multiple Histograms


```python
fig, axes = plt.subplots(1, 3, figsize=(12, 4), sharex=True, sharey=True)

for i, (name, data) in enumerate(grouped_data):
    axes[i].hist(data, bins=20, edgecolor='black', alpha=0.7)
    axes[i].set_title(name)
    axes[i].set_xlabel('Value')
    if i == 0:
        axes[i].set_ylabel('Frequency')

plt.tight_layout()
```

### Pattern 3: Side-by-Side Comparison


```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Left plot
ax1.scatter(x1, y1, alpha=0.5)
ax1.set_title('Group 1')

# Right plot
ax2.scatter(x2, y2, alpha=0.5, color='orange')
ax2.set_title('Group 2')

plt.tight_layout()
```

---

## COMMON MISTAKES

❌ **Forgetting plt.show()**


```python
# In scripts (not notebooks)
plt.plot(x, y)
# plt.show()  # Need this to display!
```

❌ **Reusing same figure**


```python
plt.plot(x, y1)
plt.plot(x, y2)  # Adds to same plot!

# Better:
plt.figure()
plt.plot(x, y1)
plt.figure()  # New figure
plt.plot(x, y2)
```

❌ **Wrong import**


```python
import matplotlib  # Wrong!
import matplotlib.pyplot as plt  # Correct
```

❌ **Modifying closed figures**


```python
plt.plot(x, y)
plt.show()
plt.xlabel('X')  # Won't work - figure is shown/closed
```

---

## TIPS FROM LECTURES

**Jittering for overplotting:**


```python
# Add small random noise to discrete variables
y_jittered = y + np.random.uniform(-0.2, 0.2, size=len(y))
plt.scatter(x, y_jittered)
```

**Transparency for dense data:**


```python
plt.scatter(x, y, alpha=0.1)  # 10% opaque
# When points overlap, color darkens
```

**Consistent colors across plots:**


```python
colors = plt.cm.tab10(range(10))  # Get 10 distinct colors
for i, data in enumerate(datasets):
    plt.plot(data, color=colors[i])
```

---

## KEY DIFFERENCES: MATPLOTLIB vs R

|Feature|Matplotlib|R (base/lattice)|
|---|---|---|
|Histogram bins|Left-closed [a,b)|Right-closed (a,b]|
|Figure creation|Explicit or implicit|Implicit|
|Subplots|fig, ax = plt.subplots()|par(mfrow=c(2,2))|
|Color transparency|alpha parameter or RGBA|rgb(r,g,b,alpha)|
|Save|plt.savefig()|png(), dev.off()|
