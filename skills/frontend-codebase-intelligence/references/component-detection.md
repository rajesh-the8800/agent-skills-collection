# Component Detection

## React / Next.js

### Functional Component
function MyComponent() {}

### Arrow Function Component
const MyComponent = () => {}

### Additional Common Patterns

export default function MyComponent() {}

export default () => <div />;

const MyComponent = memo(() => {});

const MyComponent = forwardRef((props, ref) => {});

class MyComponent extends React.Component {}

## Heuristics

- Component names start with uppercase
- JSX/TSX files indicate components
- Files inside "components/" are likely components
- Files outside `components/` may still be components
- Hook usage or JSX return statements can strengthen confidence
- Default exports in JSX or TSX files may be components even if anonymous

## Hooks Detection

Pattern:
useSomething()

Examples:
- useState
- useEffect
- useAuth (custom hook)

## Output Guidance

- Mark components as confirmed when the file clearly exports or defines a component
- Mark components as likely when only heuristics support the conclusion
- Call out wrappers such as `memo` or `forwardRef` instead of missing them
