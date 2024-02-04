import Container from 'react-bootstrap/Container';
import Stack from 'react-bootstrap/Stack';
import Sidebar from './Sidebar';

export default function Body({
    sidebar,
    children,
}: {
    sidebar: boolean;
    children: JSX.Element | JSX.Element[];
}) {
    return (
        <Container>
            <Stack direction="horizontal">
                {sidebar && <Sidebar />}
                <Container className="center-container">{children}</Container>
            </Stack>
        </Container>
    );
}
